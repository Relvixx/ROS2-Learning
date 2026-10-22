---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 07 — `parameter_node` and Runtime CLI

## Goal

Minimal Node me Parameter declare karke ROS CLI se inspect aur runtime change verify karna.

---

# Core Node Pattern

Learning implementation:

```python
import rclpy
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__('parameter_node')

        self.declare_parameter(
            'max_speed',
            2.0
        )


def main(args=None):

    rclpy.init(args=args)

    node = ParameterNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Parameter reading was studied with:

```python
self.get_parameter('max_speed').value
```

---

# Executable registration

```python
'parameter_node = my_first_pkg.parameter_node:main'
```

Conceptual chain:

```text
ros2 run
 ↓
my_first_pkg
 ↓
parameter_node executable
 ↓
main()
 ↓
ParameterNode
```

---

# Run workflow

```bash
source /opt/ros/jazzy/setup.zsh
source ~/ros2_jazzy/install/setup.zsh
```

Run node:

```bash
ros2 run my_first_pkg parameter_node
```

---

# Actual CLI Observation

```bash
ros2 param list
```

Observed:

```text
/parameter_node:
  max_speed
  start_type_description_service
  use_sim_time
```

---

# Verify default

```bash
ros2 param get /parameter_node max_speed
```

Actual:

```text
Double value is: 2.0
```

---

# Runtime change

```bash
ros2 param set /parameter_node max_speed 0.8
```

Actual:

```text
Set parameter successful
```

---

# Verify change

```bash
ros2 param get /parameter_node max_speed
```

Actual:

```text
Double value is: 0.8
```

---

# Additional observed parameter

```bash
ros2 param get /parameter_node use_sim_time
```

Actual:

```text
Boolean value is: False
```

---

# Evidence Chain

```text
Code declares
max_speed = 2.0
      ↓
CLI LIST sees it
      ↓
CLI GET confirms 2.0
      ↓
CLI SET requests 0.8
      ↓
successful
      ↓
CLI GET confirms 0.8
```

This is the key basic Parameter practical.
