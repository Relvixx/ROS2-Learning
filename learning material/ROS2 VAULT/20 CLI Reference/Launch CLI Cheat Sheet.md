---
type: cheat-sheet
status: verified
language: Hinglish
---

# ⌨️ Launch CLI Cheat Sheet

## First launch

```bash
ros2 launch my_first_pkg parameter.launch.py
```

## Multi-node launch

```bash
ros2 launch my_first_pkg multi_nodes.launch.py
```

## Verify nodes

```bash
ros2 node list
```

Actual single-node:

```text
/config_node
```

Actual multi-node:

```text
/launch_publisher
/launch_subscriber
```

## Verify launch parameter

```bash
ros2 param get /config_node max_speed
```

Actual:

```text
Double value is: 0.8
```

## Verify communication

```bash
ros2 topic info /hello_topic
```

Actual:

```text
Publisher count: 1
Subscription count: 1
```

```bash
ros2 topic echo /hello_topic
```

Actual:

```text
data: Hello from ROS2
```

---

# Build / Environment

```bash
colcon build --symlink-install --packages-select my_first_pkg
```

```bash
source /opt/ros/jazzy/setup.zsh
source ~/ros2_jazzy/install/setup.zsh
```
