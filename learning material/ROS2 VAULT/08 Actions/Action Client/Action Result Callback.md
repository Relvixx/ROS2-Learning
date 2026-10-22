---
type: callback
status: locked
depth: must-know
language: Hinglish
---

# Action Result Callback

Registered:

```python
get_result_future.add_done_callback(
    self.get_result_callback
)
```

Callback:

```python
def get_result_callback(self, future):

    result = future.result().result

    self.get_logger().info(
        f'Result: {result.sequence}'
    )
```

---

# Runtime

```text
get_result_future completes
 ↓
get_result_callback(future)
 ↓
future.result()
 ↓
Result wrapper
 ↓
.result
 ↓
Actual Fibonacci Result Object
 ↓
result.sequence
```

---

# Related
- [[future.result().result]]
- [[get_result_future]]
