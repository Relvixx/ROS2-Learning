---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `send_goal_async()`

Core:

```python
send_goal_future = self._action_client.send_goal_async(
    goal_msg,
    feedback_callback=self.feedback_callback
)
```

---

# Two important things

## 1. Goal send/initiate

```text
Goal Object
→ Action Server
```

## 2. Feedback callback register

```text
Jab Feedback aaye
→ self.feedback_callback use karo
```

---

# Return value

Returns:

```text
Future #1
```

Historical variable:

```python
send_goal_future
```

---

# Critical

`send_goal_future`:

❌ final Action Result nahi  
❌ Goal Handle immediately nahi  
❌ Feedback object nahi

It tracks the **goal request response** asynchronously.

When Future completes:

```python
goal_handle = future.result()
```

See [[send_goal_future]].
