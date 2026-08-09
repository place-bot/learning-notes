# External tools and Agent systems

## 1. Three interaction paradigms

### Passive

With constructed inputs applied, the model simply returns the content.

### Explicit tool use

The model outputs a structured tool request, and the result is returned to the model after the application is executed.

### Autonomous loop

The model repeatedly decides to call the tool or end based on the state, forming an agent.

## 2. Agent status

\[
s_t=(x,h_t,o_t,m_t),
\]

Among them, \(x\) is the target, \(h_t\) is the dialogue and action history, \(o_t\) is the observations, and \(m_t\) is the external memory.

Strategy options:

\[
a_t\sim\pi_\theta(a\mid s_t).
\]

If \(a_t\) is a tool call, it will enter \(s_{t+1}\) after execution; if it is the final answer, it will stop.

## 3. Tool definition

A tool contains at least:

- name；
- description；
- JSON schema；
- executable function；
- authorization policy；
- timeout and error semantics.

Tool descriptions are behavioral conditions for the model, and actual permissions must be controlled by code.

## 4. Guardrail and Verifier

```text
Model proposed action
→ schema validation
→ policy / permission check
→ optional human approval
→ execution
→ output sanitization
→ model observation
```

Writing "Don't do dangerous operations" in the prompt cannot replace minimum permissions, sandboxing, and manual approval.

## 5. Stop conditions

Agent must have:

- Maximum number of steps;
- token/expense budget;
- Tool timeout;
- Repeated motion detection;
- no-progress judgment;
- User cancellation;
- Paused state when manual input is required.

## 6. Memory

Short-term state is the history of this task; long-term memory is saved across tasks. Long-term memory still needs retrieval, filtering and permission judgment before entering the current context.

## 7. Orchestration software

LangChain provides higher-level agent and tool abstraction, while LangGraph prefers durable state and graph execution. They are not responsible for the underlying Transformer forward. See [LLM software stack](../llm-software-stack/index.md) for details.

## 8. Agent evaluation

|indicator|meaning|
|---|---|
| task success |Is the final task completed?|
| tool selection |Do you choose the right tool?|
| argument accuracy |Are the parameters correct?|
| excess calls |Whether unnecessary calls are generated|
| recovery |Can the tool be recovered after it fails?|
| safety violation |Whether it exceeds authority or leaks data|
| cost/latency |Resources needed to complete the task|

## 9. Boundaries of CAT Agent

Item selection is a high-constraint decision. Agents can query item banks, content labels, exposure statistics, and student status, but legal actions mask, ability estimate, and stopping rules should be executed by deterministic code. Models cannot bypass the quiz security and content blueprint.

