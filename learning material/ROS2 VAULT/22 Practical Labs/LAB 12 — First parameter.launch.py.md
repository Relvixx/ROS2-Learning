---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 12 — First `parameter.launch.py`

## Goal

Launch file se:

```text
parameter_node executable
→ /config_node
→ max_speed = 0.8
```

start/verify karna.

---

# Launch File

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    parameter_node = Node(
        package='my_first_pkg',
        executable='parameter_node',
        name='config_node',
        parameters=[
            {'max_speed': 0.8}
        ]
    )

    return LaunchDescription([
        parameter_node
    ])
```

---

# Package Preparation

`setup.py`:

```python
import os
from glob import glob
```

and:

```python
(
    os.path.join('share', package_name, 'launch'),
    glob('launch/*.launch.py')
),
```

`package.xml`:

```xml
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

---

# First Attempt

```bash
ros2 launch my_first_pkg parameter.launch.py
```

failed:

```text
file 'parameter.launch.py' was not found in the share directory...
```

See [[Launch File Not Found in Share Directory]].

---

# Fix / Rebuild

```bash
cd ~/ros2_jazzy

colcon build \
  --symlink-install \
  --packages-select my_first_pkg

source /opt/ros/jazzy/setup.zsh
source ~/ros2_jazzy/install/setup.zsh
```

Installed file verified.

---

# Successful Launch

```bash
ros2 launch my_first_pkg parameter.launch.py
```

Actual:

```text
[parameter_node-1]: process started with pid [...]
[config_node]: max_speed is: 0.8
```

---

# Independent Verification

```bash
ros2 node list
```

Actual:

```text
/config_node
```

```bash
ros2 param get /config_node max_speed
```

Actual:

```text
Double value is: 0.8
```

---

# Proven

```text
launch file installed ✅
launch action executed ✅
executable started ✅
node renamed ✅
parameter override applied ✅
```
