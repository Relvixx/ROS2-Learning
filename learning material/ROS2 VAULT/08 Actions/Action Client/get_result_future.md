---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `get_result_future`

Created:

```python
get_result_future = goal_handle.get_result_async()
```

---

# Role

> Final Action Result ready hone wali asynchronous operation ko track karta hai.

---

# Timeline

```text
Goal executing
 ↓
Feedback may arrive many times
 ↓
Server finishes
 ↓
Server marks goal success
 ↓
Result becomes available
 ↓
get_result_future completes
 ↓
get_result_callback(future)
```

---

# Critical

`send_goal_future` aur `get_result_future` alag kaam karte hain.

```text
Future #1
→ Goal response / Client Goal Handle

Future #2
→ final Result response
```

---

# Related
- [[Future]]
- [[Action Result Callback]]
