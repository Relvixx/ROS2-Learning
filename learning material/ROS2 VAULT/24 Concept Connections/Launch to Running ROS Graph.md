---
type: connection-map
status: verified
language: Hinglish
---

# Launch → Running ROS Graph

Batch 07 master map.

```text
SOURCE PACKAGE
my_first_pkg
│
├── Python executables
├── launch/
│   ├── parameter.launch.py
│   └── multi_nodes.launch.py
├── setup.py
└── package.xml
        ↓
BUILD / INSTALL
        ↓
installed package share + executables
        ↓
source setup.zsh
        ↓
ros2 launch
        ↓
Python launch file
        ↓
generate_launch_description()
        ↓
LaunchDescription Object
        ↓
Node launch actions
        ↓
processes start
        ↓
ROS graph Nodes
        ↓
Publishers / Subscribers / Parameters
        ↓
actual runtime behavior
```

---

# Parameter Path

```text
Launch Node action
parameters=[{'max_speed': 0.8}]
 ↓
parameter_node executable
 ↓
/config_node
 ↓
max_speed = 0.8
```

---

# Communication Path

```text
LaunchDescription
├── publisher action
└── subscriber action
        ↓
/launch_publisher
/launch_subscriber
        ↓
/hello_topic
        ↓
Hello from ROS2
```

Launch system orchestrates.

ROS Nodes still perform actual work.
