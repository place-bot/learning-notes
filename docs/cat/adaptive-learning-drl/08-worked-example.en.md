# Complete hand calculation and step-by-step feedback

This page constructs a hand-calculated example of continuous capabilities that illustrates how immediate progress, long-term value, TD updates, and real-time adaptation tie together. This example is constructed separately by this site for algorithm explanation and is separate from the simulation data of the paper.

## 1. Status, goals and materials

Students have two abilities:

\[
s_t=(\theta_{1t},\theta_{2t})\in[0,1]^2.
\]

The goals are:

\[
s_{\text{goal}}=(1,1).
\]

Initial state:

\[
s_0=(0,0).
\]

Three materials:

|Material|function|
|---|---|
| \(a_1\) |Builds the foundation of ability 1, increasing by up to 0.5 each time|
| \(a_2\) |Focus on improving ability 2, up to 0.7 each time|
| \(a_3\) |Comprehensive materials; the effect is significant after ability 1 reaches 0.5|

Let the deterministic transfer be:

\[
T(s,a_1)
=
\left(
\min(1,\theta_1+0.5),
\theta_2
\right),
\tag{1}
\]

\[
T(s,a_2)
=
\left(
\theta_1,
\min(1,\theta_2+0.7)
\right),
\tag{2}
\]

\[
T(s,a_3)
=
\begin{cases}
\left(
1,1
\right),
&
\theta_1\ge0.5,
\\
\left(
\min(1,\theta_1+0.1),
\min(1,\theta_2+0.1)
\right),
&
\theta_1<0.5.
\end{cases}
\tag{3}
\]

## 2. What will you choose for instant progress?

Use one step \(L_1\) gain:

\[
g(s,a)
=
\|T(s,a)-s\|_1.
\]

At \(s_0=(0,0)\):

\[
g(s_0,a_1)=0.5,
\]

\[
g(s_0,a_2)=0.7,
\]

\[
g(s_0,a_3)=0.2.
\]

The one-step greedy rule will select \(a_2\).

## 3. Long-term path comparison

### Select materials first 1

\[
(0,0)
\xrightarrow{a_1}
(0.5,0)
\xrightarrow{a_3}
(1,1).
\]

Reach the goal in two steps.

### Select materials first 2

A valid subsequent path is:

\[
(0,0)
\xrightarrow{a_2}
(0,0.7)
\xrightarrow{a_1}
(0.5,0.7)
\xrightarrow{a_3}
(1,1).
\]

Three steps to reach the goal.

The immediate capacity increment of material \(a_2\) is larger, and material \(a_1\) establishes the premise required for comprehensive materials, so the long-term strategy is to choose \(a_1\) first.

## 4. Rewards and Q-value

Rewards for continued papers:

\[
r=
\begin{cases}
-1,&s'\text{Target not reached},\\
0,&s'\text{reach goal}.
\end{cases}
\]

Take:

\[
\gamma=0.9.
\]

### Return of Material 1

The first step is to enter \((0.5,0)\), which is not terminated:

\[
r_0=-1.
\]

The second step uses \(a_3\) to reach the target:

\[
r_1=0.
\]

So:

\[
Q^*(s_0,a_1)
=
-1+0.9(0)
=
-1.
\tag{4}
\]

### Return of Material 2

The first step is to select \(a_2\):

\[
r_0=-1.
\]

In the second step, select \(a_1\), but it is still not terminated:

\[
r_1=-1.
\]

The third step is to select \(a_3\) to reach the target:

\[
r_2=0.
\]

So:

\[
Q^*(s_0,a_2)
=
-1+0.9(-1)+0.9^2(0)
=
-1.9.
\tag{5}
\]

Because:

\[
-1>-1.9,
\]

Choose \(a_1\) as a long-term strategy.

## 5. Bellman decomposition

Select \(a_1\) from \(s_0\) and enter

\[
s_1=(0.5,0).
\]

In \(s_1\), comprehensive materials reach the target directly:

\[
Q^*(s_1,a_3)=0.
\]

Bellman's equation gives:

\[
Q^*(s_0,a_1)
=
-1
+0.9
\max_aQ^*(s_1,a)
=
-1.
\]

Select \(a_2\) from \(s_0\) and enter

\[
\widetilde s_1=(0,0.7).
\]

This state still requires a non-terminating transfer:

\[
\max_aQ^*(\widetilde s_1,a)=-1.
\]

Therefore:

\[
Q^*(s_0,a_2)
=
-1+0.9(-1)
=
-1.9.
\]

## 6. A TD update

Assume training an early network prediction:

\[
\widehat Q(s_0,a_1)=-0.2.
\]

Real interaction observed:

\[
(s_0,a_1,-1,s_1).
\]

The target network currently gives:

\[
\max_{a'}\widehat Q(s_1,a')=-0.1.
\]

TD target：

\[
y
=
-1+0.9(-0.1)
=
-1.09.
\]

TD error:

\[
\delta
=
y-\widehat Q(s_0,a_1)
=
-1.09-(-0.2)
=
-0.89.
\]

The current prediction is too optimistic and the gradient update will reduce \(\widehat Q(s_0,a_1)\).

## 7. How student feedback changes next steps

Now add learning randomness. After selecting \(a_1\), two measurement results may appear:

\[
s_1^{(A)}=(0.55,0.05),
\]

\[
s_1^{(B)}=(0.30,0.05).
\]

To student A:

\[
\theta_1=0.55\ge0.5,
\]

DQN may select composite material \(a_3\).

To student B:

\[
\theta_1=0.30<0.5,
\]

DQN may again select \(a_1\).

The initial actions are the same, the real feedback in the first round is different, and the path in the second round immediately bifurcates:

```text
s0 ──a1──► s1(A) ──a3──► ...
 │
 └─a1──► s1(B) ──a1──► ...
```

This is policy-level adaptation.

## 8. Action changes caused by measurement errors

The student’s true status may be:

\[
s=(0.52,0.10),
\]

The measurement estimate is:

\[
\widehat s=(0.47,0.10).
\]

The real state has reached the advanced threshold of comprehensive materials, and the estimated state is still below the threshold. If the strategy only uses point estimates, one more \(a_1\) may be scheduled.

Possible improvements include:

- Enter the ability posterior mean and variance into the strategy together;
- Adopt risk-sensitive actions for critical conditions;
- Reduce estimate variance with short CAT;
- Keep recent answers and material history in status.

## 9. How to join transition model

Fitting from real data:

\[
\widehat s'
=
\psi_v(s,a).
\]

If the model predicts at \(s_0,a_1\):

\[
\psi_v(s_0,a_1)=(0.48,0.04),
\]

DQN can continue to select the next action in the virtual environment and generate training trajectories. When the model output is low, the strategy will underestimate the pre-revision value of \(a_1\), indicating that the transition model error will be passed to the strategy.

## 10. Complete information flow of the example

\[
\boxed{
\begin{aligned}
\text{Measurement status}s_t
&\longrightarrow
\text{DQN output}\widehat Q(s_t,\cdot)
\\
&\longrightarrow
\text{Select material}a_t
\\
&\longrightarrow
\text{real student or}\psi_v\text{produce}s_{t+1}
\\
&\longrightarrow
\text{Calculate}r_t
\\
&\longrightarrow
\text{save}(s_t,a_t,r_t,s_{t+1})
\\
&\longrightarrow
\text{TD updated and moved on to next round}.
\end{aligned}
}
\]
