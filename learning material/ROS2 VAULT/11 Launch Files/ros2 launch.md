---
type: cli-reference
status: verified
depth: must-know
language: Hinglish
---

# `ros2 launch`

Basic syntax:

```bash
ros2 launch <package> <launch_file>
```

Actual:

```bash
ros2 launch my_first_pkg parameter.launch.py
```

and:

```bash
ros2 launch my_first_pkg multi_nodes.launch.py
```

---

# What happens?

```text
package locate
 ↓
installed launch file locate
 ↓
Python launch description load
 ↓
generate_launch_description()
 ↓
LaunchDescription
 ↓
actions execute
```

---

# Important distinction from `ros2 run`

```bash
ros2 run my_first_pkg publisher_node
```

→ one executable manually start intent.

```bash
ros2 launch my_first_pkg multi_nodes.launch.py
```

→ launch description execute; can start/configure multiple components.

Launch is orchestration layer, not merely alternate spelling of `ros2 run`.
