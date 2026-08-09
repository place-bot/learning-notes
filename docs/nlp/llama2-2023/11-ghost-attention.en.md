#Ghost Attention and multi-round consistency

## 1. Question

System instructions often require that the entire conversation continue to comply with constraints, such as:

- Always in French;
- Answer briefly;
- Play a character;
-Stay consistent.

Early RLHF models would forget the first round of instructions after a few rounds. Although the system message is still in the context, the model has not learned to treat it as a high-priority condition long-term.

## 2. Dialogue representation

Multiple rounds of data are written as:

\[
[u_1,a_1,u_2,a_2,\ldots,u_n,a_n],
\]

The global instruction is \(I\). Desirable behavior requirements:

\[
a_t\sim p_\theta(a_t\mid I,u_1,a_1,\ldots,u_t)
\]

All \(t\) are continuously subject to \(I\).

## 3. GAtt data structure

The first step is to spell out the instructions for each user turn in the synthesized version:

\[
[I+u_1,a_1,I+u_2,a_2,\ldots,I+u_n].
\]

Let the latest RLHF model generate the final answer \(a_n^+\) in this strong reminder context.

In the second step, the training input only retains instructions from the first round:

\[
[I+u_1,a_1,u_2,a_2,\ldots,u_n,a_n^+].
\]

Set the loss of tokens in all previous rounds to zero, and only backpropagate the final answer. The model learns to reproduce the behavior of the strong reminder version without repeated reminders round by round.

## 4. Why is it called Ghost Attention?

The training goal is to have later responses continue to rely on initial instructions that have moved away from the current position. The command does not actually appear every round, but continues to affect the dialogue like a "ghost".

The attention visualization of the paper shows that the GAtt model maintains strong attention activation for system instructions in longer conversations. This is evidence of a related mechanism and cannot prove that a single attention weight can fully explain the behavior.

## 5. Synthetic constraints

Training use:

- hobbies；
- language；
- public figure。

The final instruction randomly combines multiple constraints, and has a half probability of being changed to a shorter expression, such as compressing the complete role-playing instruction into a short label to increase the diversity of wording.

## 6. Generalization

Constraints that GAtt does not appear directly in training, such as "Always answer with Haiku", can also show some zero-shot continuation. The paper report can maintain consistency for more than 20 rounds before reaching the 4K context limit.

## 7. The key role of Loss mask

If loss is also calculated for all historical assistant answers during training, these old answers may come from the original dialogue without GAtt behavior and are inconsistent with the new system instructions. Set the historical token loss to zero, and training only requires that the last answer follows the system message:

\[
\mathcal L_{\mathrm{GAtt}}
=
-\sum_{t\in a_n^+}
\log p_\theta(t\mid I,\text{history}).
\]

## 8. Limitations

- Commands are still restricted by the 4096-token window;
- Fewer types of training constraints;
- Conflicting priorities of system/user directives are not fully resolved;
- The paper version does not support formal modification of the system message mid-conversation;
- The security of long conversations may be reduced;
- Sustained attention does not guarantee that the facts and task status are correct.

The value of GAtt is to turn "multiple rounds of remembering system instructions" into a specialized data construction and loss mask problem.
