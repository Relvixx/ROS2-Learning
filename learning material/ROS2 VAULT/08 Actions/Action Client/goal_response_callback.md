---
type: callback
status: locked
depth: must-know
language: Hinglish
---

# `goal_response_callback()`

Registered:

```python
send_goal_future.add_done_callback(
    self.goal_response_callback
)
```

Meaning:

> Jab Goal request Future complete ho, ye callback execute karo.

---

# Callback

```python
def goal_response_callback(self, future):

    goal_handle = future.result()

    if not goal_handle.accepted:
        self.get_logger().info('Goal rejected')
        return

    self.get_logger().info('Goal accepted')

    get_result_future = goal_handle.get_result_async()

    get_result_future.add_done_callback(
        self.get_result_callback
    )
```

---

# Runtime

```text
send_goal_future complete
 ↓
goal_response_callback(future)
 ↓
future.result()
 ↓
Client Goal Handle
 ↓
accepted?
 ├── No → stop result flow
 └── Yes
      ↓
 get_result_async()
```

---

# Related
- [[Client Goal Handle]]
- [[get_result_async]]
