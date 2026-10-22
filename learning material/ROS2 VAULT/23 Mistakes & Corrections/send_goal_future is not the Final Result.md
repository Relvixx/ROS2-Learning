---
type: correction
status: canonical
language: Hinglish
---

# `send_goal_future` is not the Final Result

Wrong:

```text
send_goal_async()
 ↓
Future
 ↓
Final Result
```

❌

Correct:

```text
Goal Object
 ↓
send_goal_async()
 ↓
send_goal_future
 ↓
Goal response
 ↓
Client Goal Handle
 ↓
get_result_async()
 ↓
get_result_future
 ↓
Final Result
```

---

# Why two Futures?

```text
Future #1
→ Goal request response

Future #2
→ final Result response
```

See [[send_goal_future]] and [[get_result_future]].
