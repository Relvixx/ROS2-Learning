---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `spin_until_future_complete()`

Common Service Client pattern studied:

```python
rclpy.spin_until_future_complete(self, future)
```

---

# Simple meaning

> ROS events/processes ko handle karte raho jab tak specific Future complete nahi ho jata.

---

# Flow

```text
call_async(request)
      ↓
Future
      ↓
spin_until_future_complete(...)
      ↓
ROS events process
      ↓
Response arrives
      ↓
Future complete
      ↓
future.result()
      ↓
Response Object
```

---

# `spin()` vs `spin_until_future_complete()`

## `rclpy.spin(node)`

```text
Node
 ↓
continuously process callbacks/events
```

## `spin_until_future_complete(node, future)`

```text
Node + specific Future
 ↓
process ROS events
 ↓
Future complete?
  ├── No → continue
  └── Yes → return
```

---

# Related

- [[rclpy spin]]
- [[Future]]
- [[Service Client]]
