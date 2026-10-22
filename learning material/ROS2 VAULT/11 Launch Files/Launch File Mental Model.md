---
type: mental-model
status: verified
depth: must-know
language: Hinglish
---

# Launch File Mental Model

Launch file khud robot ka kaam nahi karti.

Better:

```text
Launch File
→ instructions / orchestration description

Running Nodes
→ actual computation / communication
```

---

# Runtime Story

```text
ros2 launch
 ↓
Python launch file load
 ↓
generate_launch_description()
 ↓
LaunchDescription Object
 ↓
contains launch actions
 ↓
Launch system executes actions
 ↓
executables/processes start
 ↓
ROS Nodes appear in graph
```

---

# Example

```python
return LaunchDescription([
    Node(
        package='my_first_pkg',
        executable='parameter_node',
        name='config_node'
    )
])
```

Meaning:

```text
"my_first_pkg ka parameter_node executable start karo
aur running ROS node ko config_node naam do"
```

See [[Launch Action Node Object]].
