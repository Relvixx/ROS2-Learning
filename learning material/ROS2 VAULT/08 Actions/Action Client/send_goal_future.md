---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `send_goal_future`

Created by:

```python
send_goal_future = self._action_client.send_goal_async(...)
```

---

# Role

> Goal request ke response ko asynchronously track karta hai.

---

# Timeline

```text
Goal Object
 ↓
send_goal_async()
 ↓
send_goal_future
 ↓
Server responds to goal request
 ↓
Future completes
 ↓
goal_response_callback(future)
 ↓
future.result()
 ↓
Client Goal Handle
```

---

# Important correction

Early loose wording:

> "Future batata hai Goal successfully bhej diya."

Better:

> Future goal-request response ko track karta hai. Completed Future ke `result()` se Client Goal Handle milta hai; us handle ke `accepted` property se accept/reject pata chalta hai.

---

# Related
- [[Future]]
- [[goal_response_callback]]
- [[Client Goal Handle]]
- [[send_goal_future is not the Final Result]]
