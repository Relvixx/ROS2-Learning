---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Action Interface

ROS 2 Interface hierarchy:

```text
ROS 2 Interface
├── Message Interface (.msg)
├── Service Interface (.srv)
└── Action Interface (.action)
```

Action Interface defines:

```text
Goal
---
Result
---
Feedback
```

---

# Important

Action Interface actual task logic nahi likhta.

Ye sirf data contract/shape define karta hai.

Fibonacci calculate karne ka algorithm `.action` file me nahi hota.

---

# Structure

```text
Goal fields
---
Result fields
---
Feedback fields
```

Do separators important hain.

---

# Generated concepts

Conceptually interface se generated types available hote hain:

```python
Fibonacci.Goal()
Fibonacci.Result()
Fibonacci.Feedback()
```

---

# Related
- [[Fibonacci Action Interface]]
- [[Goal Object]]
- [[Feedback Object]]
- [[Action Result Object]]
