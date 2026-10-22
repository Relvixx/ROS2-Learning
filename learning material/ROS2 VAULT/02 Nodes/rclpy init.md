---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `rclpy.init()`

## Simple meaning

`init` = initialize.

```python
rclpy.init(args=args)
```

Learning mental model:

> ROS 2 Python client side ko initialize/ready karo taaki Nodes aur ROS communication functionality use ki ja sake.

---

# Runtime order

```text
ros2 run
   ↓
main()
   ↓
rclpy.init()
   ↓
SimpleNode()
   ↓
rclpy.spin(node)
   ↓
shutdown
```

Important:

> Node object create karne se pehle `rclpy.init()` hota hai.

---

# Agar hata dein?

Historical quiz me expected understanding:

```text
ROS initialization missing
↓
Node creation/use par runtime problem
```

Exact internal error text memorize karna goal nahi.

---

# `args=args`

Learning time par isko intentionally deep nahi kiya gaya tha.

Focus:

```python
rclpy.init()
```

ka role.

CLI argument processing later expand ki ja sakti hai.

---

# Knowledge Boundary

## 🟢 Must know

- Initialize = ROS Python environment ready karna.
- Node creation se pehle.
- ROS communication/context setup ka entry step.

## 🔴 Abhi nahi

- `rcl_context_t`
- RMW initialization
- DDS participant internals
- allocator internals

---

# Related

- [[First Node Anatomy]]
- [[Node Runtime Flow]]
