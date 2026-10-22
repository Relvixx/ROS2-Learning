---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `get_result_async()`

Goal accepted hone ke baad:

```python
get_result_future = goal_handle.get_result_async()
```

---

# Meaning

> Accepted goal ka final Result asynchronously request/track karo.

---

# Output

Returns:

```text
Future #2
```

Historical name:

```python
get_result_future
```

---

# Important order

```text
send_goal_async()
 ↓
send_goal_future completes
 ↓
Client Goal Handle
 ↓
accepted
 ↓
get_result_async()
 ↓
get_result_future
```

`get_result_future` Goal Handle milne se pehle create nahi hota in this learned flow.

---

# Related
- [[get_result_future]]
- [[Client Goal Handle]]
