---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Server Goal Handle

Server execute callback:

```python
def execute_callback(self, goal_handle):
```

Yahan `goal_handle` server-side runtime object hai jo currently accepted/executing Goal ko represent/manage karta hai.

---

# Structure Mental Model

```text
server goal_handle
├── request
│    └── order
├── publish_feedback(...)
└── succeed()
```

---

# Why useful?

Server ko sirf Goal data nahi chahiye.

Usko execution ke dauran:

```text
Goal request read
Feedback send
Goal state update
```

karna hota hai.

Isliye Goal Handle object useful hai.

---

# Goal vs Server Goal Handle

```text
Goal Object
→ requested data

Server Goal Handle
→ accepted/executing goal ka runtime management object
```

---

# Important Client Distinction

Action Client me bhi variable ka naam `goal_handle` tha, lekin wo client-side handle object tha.

Server aur client handles same runtime role nahi.

See [[Client Goal Handle]].
