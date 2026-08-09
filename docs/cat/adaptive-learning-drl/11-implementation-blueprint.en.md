# Implementation blueprint and checklist

The paper gives algorithm pseudocode and does not provide a confirmable official public code repository. This page organizes reproducible implementations based on the first draft Algorithm 1, network description and experimental parameters, and separately marks the project selections not specified in the paper.

## 1. Recommended module boundaries

```text
AbilityEstimator
    └── responses -> state

StudentEnvironment
    └── (state, material) -> next_state

TransitionModel
    └── fit real transitions
    └── (state, material) -> predicted next_state

QNetwork
    └── state -> Q value for every material

ReplayBuffer
    └── store and sample transitions

DQNTrainer
    └── exploration, TD target, optimization
```

Module separation facilitates independent verification of measurement errors, environmental errors, and strategy errors.

## 2. transition data structure

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class Transition:
    state: np.ndarray
    action: int
    reward: float
    next_state: np.ndarray
    terminated: bool
    truncated: bool
```

It is recommended to distinguish:

- `terminated`: Achieve capability target;
- `truncated`: Maximum number of rounds reached or external interrupt.

The bootstrap rules for the two can be different.

## 3. Paper simulation environment

The following uses the remaining capacity space to scale the Beta increment, corresponding to:

\[
\Delta\theta_d=(1-\theta_d)Z_d.
\]

```python
import numpy as np

class SimulatedLearner:
    def __init__(self, rng, threshold=1e-3):
        self.rng = rng
        self.threshold = threshold
        self.state = np.zeros(2, dtype=np.float32)

    def reset(self):
        self.state = np.zeros(2, dtype=np.float32)
        return self.state.copy()

    def _g1(self, state, action):
        theta1, theta2 = state
        if action == 0:
            return 3 + 8 * theta1 - 0.2 * theta2
        if action == 2:
            return 15 + 15 * theta1 - 0.4 * theta2
        return None

    def _g2(self, state, action, delta1):
        theta1, theta2 = state
        if action == 1:
            return 10 - theta1 + 5 * theta2
        if action == 2:
            bump = np.exp(-((theta1 - 0.6) ** 2) / 0.3)
            return (
                20
                - 28 * theta1 * bump
                + 30 * theta2
                - 0.3 * delta1
            )
        return None

    def step(self, action):
        theta1, theta2 = self.state

        delta1 = 0.0
        if action in (0, 2):
            z1 = self.rng.beta(1.0, self._g1(self.state, action))
            delta1 = (1.0 - theta1) * z1

        delta2 = 0.0
        if action in (1, 2):
            z2 = self.rng.beta(
                1.0,
                self._g2(self.state, action, delta1),
            )
            delta2 = (1.0 - theta2) * z2

        next_state = np.clip(
            self.state + np.array([delta1, delta2]),
            0.0,
            1.0,
        ).astype(np.float32)

        terminated = np.max(np.abs(next_state - 1.0)) < self.threshold
        reward = 0.0 if terminated else -1.0
        self.state = next_state
        return next_state.copy(), reward, terminated
```

!!! warning "recurrence selection"

    The paper does not clearly state how the beta sample maps to \([0,1-\theta_d]\). The remaining space scaling above is a reasonable implementation and should not be taken as confirmed behavior of the author's code.

## 4. Q Network

The structure of the paper is two-dimensional input, 64 and 32 unit hidden layers, and three-dimensional output:

```python
import torch
from torch import nn

class QNetwork(nn.Module):
    def __init__(self, state_dim=2, action_dim=3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, action_dim),
        )

    def forward(self, state):
        return self.net(state)
```

The output layer does not use softmax. Q-values ​​are real long-term values ​​and do not need to sum to 1.

## 5. Experience replay

```python
from collections import deque
import random

class ReplayBuffer:
    def __init__(self, capacity):
        self.data = deque(maxlen=capacity)

    def add(self, transition):
        self.data.append(transition)

    def sample(self, batch_size):
        return random.sample(self.data, batch_size)

    def __len__(self):
        return len(self.data)
```

The paper does not report buffer capacity and warm-up length. Recurrence should be explicitly recorded in the configuration file.

## 6. epsilon scheduling

```python
def epsilon_at_step(
    step,
    epsilon_start=1.0,
    epsilon_end=0.1,
    decay_steps=2000,
):
    fraction = min(step / decay_steps, 1.0)
    return (
        epsilon_start
        - (epsilon_start - epsilon_end) * fraction
    )
```

Action selection:

```python
def select_action(q_network, state, epsilon, rng, valid_mask=None):
    if rng.random() < epsilon:
        if valid_mask is None:
            return int(rng.integers(0, 3))
        candidates = np.flatnonzero(valid_mask)
        return int(rng.choice(candidates))

    state_tensor = torch.as_tensor(
        state, dtype=torch.float32
    ).unsqueeze(0)

    with torch.no_grad():
        q_values = q_network(state_tensor).squeeze(0)

    if valid_mask is not None:
        mask = torch.as_tensor(valid_mask, dtype=torch.bool)
        q_values = q_values.masked_fill(~mask, float("-inf"))

    return int(torch.argmax(q_values).item())
```

## 7. Batch TD update

Modern stable releases use target network:

```python
import torch.nn.functional as F

def dqn_update(
    online_q,
    target_q,
    optimizer,
    batch,
    gamma=0.9,
):
    states = torch.as_tensor(
        np.stack([x.state for x in batch]),
        dtype=torch.float32,
    )
    actions = torch.as_tensor(
        [x.action for x in batch],
        dtype=torch.long,
    )
    rewards = torch.as_tensor(
        [x.reward for x in batch],
        dtype=torch.float32,
    )
    next_states = torch.as_tensor(
        np.stack([x.next_state for x in batch]),
        dtype=torch.float32,
    )
    terminated = torch.as_tensor(
        [x.terminated for x in batch],
        dtype=torch.float32,
    )

    predicted = online_q(states).gather(
        1, actions[:, None]
    ).squeeze(1)

    with torch.no_grad():
        next_value = target_q(next_states).max(dim=1).values
        target = rewards + gamma * (1.0 - terminated) * next_value

    loss = F.mse_loss(predicted, target)

    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(online_q.parameters(), 10.0)
    optimizer.step()
    return float(loss.item())
```

When replicating the paper using bootstrap on the same network, `online_q` can be used to calculate `next_value`; this difference should be written into the experimental report.

## 8. transition model

```python
class TransitionModel(nn.Module):
    def __init__(self, state_dim=2, action_dim=3):
        super().__init__()
        self.action_dim = action_dim
        self.net = nn.Sequential(
            nn.Linear(state_dim + action_dim, 32),
            nn.ReLU(),
            nn.Linear(32, state_dim),
            nn.Sigmoid(),
        )

    def forward(self, state, action):
        one_hot = F.one_hot(
            action,
            num_classes=self.action_dim,
        ).float()
        inputs = torch.cat([state, one_hot], dim=-1)
        return self.net(inputs)
```

Training loss:

\[
\mathcal L_{\text{transition}}
=
\frac1H
\sum_{i=1}^{H}
\|
\psi_v(s_i,a_i)-s_i'
\|_2^2.
\]

To enforce monotonicity, let the network output non-negative increments, clipped to the remaining capacity space.

## 9. Ability estimate interface of real system

```python
class AbilityEstimator:
    def fit_or_update(self, responses, item_bank):
        """
        Return:
            mean: posterior/MAP/EAP ability estimate
            uncertainty: covariance or standard error
        """
        raise NotImplementedError
```

It is recommended to save:

- Ability point estimation;
- standard error or posterior covariance;
- Number of test questions;
- model fit status;
- Ability scale version.

Saving just a floating point vector loses critical measurement information.

## 10. Training log

Each episode records at least:

|Field|Purpose|
|---|---|
| episode reward |strategy performance|
| episode length |Goal arrival efficiency|
| epsilon |Explore status|
| TD loss |Optimize diagnosis|
|Q mean and range|Overestimation and divergence checks|
|Action frequency|material coverage|
|termination rate|Does it time out frequently?|
|status override|extrapolation risk|
|transition model \(R^2\)/RMSE|model fit|
|multi-step rollout error|Long track reliability|

## 11. Minimal testing

### Math Test

- The target status reward is 0;
- The non-target status reward is \(-1\);
- terminal target without bootstrap;
- epsilon decay endpoint is correct;
- Unable to select illegal actions after masking.

### Environment testing

- Status is always at \([0,1]^D\);
- \(s_{t+1}\ge s_t\) under the monotonic assumption;
- Random seeds can be reproduced;
- Each episode has a maximum number of steps.

### Strategy Test

- The fully random strategy is a reproducible baseline;
- The optimal action in the manual environment is consistent with the analytical result;
- The target network synchronization frequency is correct;
- The output of the strategy loaded after saving is consistent.

## 12. Paper reproduction and engineering enhancement should be separated

It is recommended to report two sets of configurations:

|Configuration|purpose|
|---|---|
| Paper-like |Try to follow the same target, network and hyperparameter of the same paper as possible|
| Stable DQN |target network, Double DQN, gradient clipping, clear truncation|

Replicating the conclusion of the paper first, and then judging whether the engineering enhancement improves the result can avoid mistaking algorithm differences for recurrence errors.

## 13. Realistic deployment threshold

Before going online, you need to:

1. A collection of legal actions reviewed by content experts;
2. Offline coverage and counterfactual evaluation;
3. Transition model uncertainty monitoring;
4. Teacher overwrite and safe rollback;
5. Student exit, load and equity indicators;
6. Versioned capability scale and material library;
7. Controlled online testing.
