---
type: runtime-flow
status: verified
depth: must-know
language: Hinglish
---

# Single Node Launch Runtime Flow

File:

```text
parameter.launch.py
```

Code core:

```python
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

# Runtime

```text
ros2 launch my_first_pkg parameter.launch.py
 ↓
launch file load
 ↓
generate_launch_description()
 ↓
Node launch-action object created
 ↓
LaunchDescription returned
 ↓
launch action executes
 ↓
parameter_node executable starts
 ↓
ROS graph node = /config_node
 ↓
startup max_speed = 0.8
```

---

# Actual Evidence

Launch terminal:

```text
[parameter_node-1]: process started ...
[config_node]: max_speed is: 0.8
```

CLI:

```text
ros2 node list
→ /config_node
```

```text
ros2 param get /config_node max_speed
→ Double value is: 0.8
```
