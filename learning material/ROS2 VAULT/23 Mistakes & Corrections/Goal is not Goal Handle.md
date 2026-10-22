---
type: correction
status: canonical
language: Hinglish
---

# Goal is not Goal Handle

## Goal Object

```python
goal_msg = Fibonacci.Goal()
goal_msg.order = 5
```

Meaning:

> Requested task/data.

---

# Goal Handle

Runtime object representing/managing goal relationship.

But server and client handles ko bhi distinguish karo.

## Server-side

```text
request
publish_feedback()
succeed()
```

## Client-side

```text
accepted
get_result_async()
```

---

# Correct hierarchy

```text
Goal Object
→ requested task

Server Goal Handle
→ server execution/goal management

Client Goal Handle
→ client-side accepted goal handle
```

See [[Server Goal Handle]] and [[Client Goal Handle]].
