---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Multi Node Launch

File:

```text
multi_nodes.launch.py
```

Code:

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    publisher = Node(
        package='my_first_pkg',
        executable='publisher_node',
        name='launch_publisher'
    )

    subscriber = Node(
        package='my_first_pkg',
        executable='subscriber_node',
        name='launch_subscriber'
    )

    return LaunchDescription([
        publisher,
        subscriber
    ])
```

---

# Object Meaning

```text
publisher
→ Node launch-action object reference

subscriber
→ Node launch-action object reference
```

Not actual Publisher / Subscription objects.

---

# Orchestration

```text
LaunchDescription
├── publisher launch action
└── subscriber launch action
```

One launch command → two processes/nodes started.
