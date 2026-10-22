---
type: runtime-flow
status: verified
depth: must-know
language: Hinglish
---

# Build → Install → Source → Launch Flow

After adding launch files:

```bash
cd ~/ros2_jazzy

colcon build \
  --symlink-install \
  --packages-select my_first_pkg
```

Then:

```bash
source /opt/ros/jazzy/setup.zsh
source ~/ros2_jazzy/install/setup.zsh
```

Then:

```bash
ros2 launch my_first_pkg parameter.launch.py
```

---

# Full Mental Model

```text
Source launch file
 ↓
setup.py knows installation rule
 ↓
colcon build/install
 ↓
launch file appears in install share
 ↓
workspace sourced
 ↓
package discoverable
 ↓
ros2 launch finds installed launch file
 ↓
launch actions execute
```

This flow came directly from real debugging.

See [[Launch File Not Found in Share Directory]].
