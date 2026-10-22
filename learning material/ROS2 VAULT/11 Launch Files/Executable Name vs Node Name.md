---
type: correction
status: verified
depth: must-know
language: Hinglish
---

# Executable Name ≠ Node Name

Actual first launch:

```text
Executable:
parameter_node

Running ROS Node name:
/config_node
```

Launch:

```python
Node(
    package='my_first_pkg',
    executable='parameter_node',
    name='config_node'
)
```

---

# Multi-node practical

```text
publisher executable
→ publisher_node

running node
→ /launch_publisher
```

```text
subscriber executable
→ subscriber_node

running node
→ /launch_subscriber
```

---

# Why important?

CLI aur debugging me:

```text
ros2 pkg executables
```

executable names dekh sakta hai.

```text
ros2 node list
```

running ROS node names dikhata hai.

Same layer nahi.
