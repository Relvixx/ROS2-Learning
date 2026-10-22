---
type: runtime-flow
status: verified
depth: must-know
language: Hinglish
---

# Multi Node Launch Runtime Flow

```text
ros2 launch my_first_pkg multi_nodes.launch.py
        ↓
launch file load
        ↓
generate_launch_description()
        ↓
LaunchDescription Object
        ↓
contains 2 Node launch actions
        ↓
┌────────────────────┬────────────────────┐
↓                    ↓
publisher_node       subscriber_node
process starts       process starts
↓                    ↓
/launch_publisher    /launch_subscriber
        │                    │
        └──── /hello_topic ──┘
                 ↓
         Hello from ROS2
```

---

# Actual Launch Output

```text
publisher_node process started
subscriber_node process started
```

After bug fix:

```text
[launch_publisher]: Hello from ROS2
[launch_subscriber]: Hello from ROS2
```

---

# Graph Verification

```text
/launch_publisher
/launch_subscriber
```

Topic:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

Data:

```text
Hello from ROS2
```

See [[LAB 14 — Launch Graph and Topic Verification]].
