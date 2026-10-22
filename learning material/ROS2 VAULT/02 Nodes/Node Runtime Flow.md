---
type: runtime-flow
status: locked
depth: must-know
language: Hinglish
---

# Node Runtime Flow

Ye note code ko execution story me convert karta hai.

---

# Command

```bash
ros2 run my_first_pkg simple_node
```

---

# High-level runtime

```text
Terminal
   ↓
ros2 CLI
   ↓
installed package/executable locate
   ↓
Python console-script executable
   ↓
my_first_pkg.simple_node import
   ↓
main()
   ↓
rclpy.init()
   ↓
SimpleNode()
   ↓
SimpleNode.__init__()
   ↓
Node base initialization
   ↓
logger message
   ↓
rclpy.spin(node)
   ↓
Executor processes events/callbacks
```

---

# Object creation trace

```python
node = SimpleNode()
```

Breakdown:

```text
SimpleNode
 ↓ class

SimpleNode()
 ↓ instantiate

node
 ↓ object reference
```

Constructor path:

```text
SimpleNode()
   ↓
SimpleNode.__init__(self)
   ↓
super().__init__("simple_node")
   ↓
ROS Node side initialize
```

---

# Why `main()` important?

Program startup steps ek organized place me hote hain.

See [[main Function]].

---

# Why `rclpy.init()` before Node?

ROS Python client environment initialize karna hota hai.

See [[rclpy init]].

---

# Why `spin()`?

Event/callback processing.

See [[rclpy spin]].

---

# Why this runtime view useful hai?

Future me Publisher code dekhne par:

```text
Node create
 ↓
Publisher object create
 ↓
Timer create
 ↓
spin
 ↓
Timer event
 ↓
callback
 ↓
publish
```

Subscriber me:

```text
Node create
 ↓
Subscription create
 ↓
spin
 ↓
Message event
 ↓
callback
```

Service/Action me bhi same Node + callback runtime foundation reuse hota hai.

---

# One-line recall

> `ros2 run` executable start karta hai → `main()` startup control leta hai → `rclpy.init()` ROS ready karta hai → Node object banta hai → `spin()` executor ko callbacks/events process karne deta hai.
