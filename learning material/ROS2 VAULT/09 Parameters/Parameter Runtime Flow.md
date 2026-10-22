---
type: runtime-flow
status: verified
depth: must-know
language: Hinglish
---

# Parameter Runtime Flow

## Node startup

```text
ros2 run my_first_pkg parameter_node
 ↓
main()
 ↓
rclpy.init()
 ↓
ParameterNode()
 ↓
declare_parameter('max_speed', 2.0)
 ↓
max_speed exists
 ↓
rclpy.spin(node)
```

---

# Reading

```text
Node
 ↓
get_parameter('max_speed')
 ↓
Parameter Object
 ↓
.value
 ↓
2.0
```

---

# Runtime CLI set

```text
CLI
ros2 param set /parameter_node max_speed 0.8
 ↓
ROS parameter system
 ↓
running /parameter_node
 ↓
current max_speed becomes 0.8
 ↓
CLI get
 ↓
Double value is: 0.8
```

---

# Current chapter boundary

At this point:

```text
set request
→ accepted
```

was enough.

Next chapter inserts validation:

```text
set request
 ↓
callback
 ↓
valid?
 ├── yes → accept
 └── no  → reject
```
