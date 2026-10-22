---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# ActionClient Object

Typical:

```python
self._action_client = ActionClient(
    self,
    Fibonacci,
    'fibonacci'
)
```

---

# Arguments

```text
self
→ current client Node

Fibonacci
→ Action Interface/type

'fibonacci'
→ Action name
```

---

# Important

Is line par Goal send nahi hota.

Sirf client resource configure/create hota hai.

Goal later:

```python
send_goal_async(...)
```

se send/initiate hota hai.

---

# Object Tree

```text
FibonacciActionClient Node
└── _action_client
      ↓
   ActionClient Object
```

---

# Related
- [[send_goal_async]]
- [[wait_for_server Action]]
