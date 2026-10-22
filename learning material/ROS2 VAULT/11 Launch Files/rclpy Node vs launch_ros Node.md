---
type: correction
status: verified
depth: must-know
language: Hinglish
---

# `rclpy.node.Node` vs `launch_ros.actions.Node`

Dono ka naam `Node` hai, lekin same class/role nahi.

---

# ROS Node Code

```python
from rclpy.node import Node
```

Used:

```python
class PublisherNode(Node):
    ...
```

Meaning:

> Actual ROS Node base class.

---

# Launch File

```python
from launch_ros.actions import Node
```

Used:

```python
publisher = Node(
    package='my_first_pkg',
    executable='publisher_node'
)
```

Meaning:

> Launch action/instruction describing a ROS node executable to start.

---

# Mental Model

```text
rclpy.node.Node
→ actual ROS node programming class

launch_ros.actions.Node
→ launch-system action
```

Same word, different namespace, different role.

This distinction Rahul correctly identified during learning.
