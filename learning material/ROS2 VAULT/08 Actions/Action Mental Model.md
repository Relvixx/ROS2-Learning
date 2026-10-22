---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Action Mental Model

## Master Flow

```text
ACTION CLIENT
    │
    │ Goal
    ▼
ACTION SERVER
    │
    │ accept / reject
    ▼
Execution
    │
    ├──── Feedback ────→ Client
    ├──── Feedback ────→ Client
    ├──── Feedback ────→ Client
    │
    ▼
Goal succeeds
    │
    └──── Final Result ─→ Client
```

---

# Important distinction

Action me ek hi "response" object wali simple Service story nahi.

Client side par do async stages important hue:

```text
Goal request
   ↓
send_goal_future
   ↓
Client Goal Handle
   ↓
get_result_async()
   ↓
get_result_future
   ↓
Final Result
```

Feedback parallel event stream ki tarah registered callback me aata hai.

---

# 3 Pipelines

```text
PIPELINE 1 — GOAL
Goal → send_goal_async → Future #1 → Goal Handle

PIPELINE 2 — FEEDBACK
Server Feedback → feedback_callback

PIPELINE 3 — RESULT
Goal Handle → get_result_async → Future #2 → Result
```

See [[Action Client Three Pipelines]].
