---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# `generate_launch_description()`

Typical Python launch file:

```python
def generate_launch_description():
    return LaunchDescription([
        ...
    ])
```

ROS 2 launch system is expected function ko call karta hai.

---

# Return

Function returns:

```text
LaunchDescription Object
```

---

# Runtime

```text
ros2 launch ...
 ↓
launch file loaded
 ↓
generate_launch_description()
 ↓
LaunchDescription returned
 ↓
launch actions executed
```

---

# Python Category

```text
generate_launch_description
→ function

LaunchDescription(...)
→ object creation

Node(...)
→ launch-action object creation
```

Nested reasoning:

```text
function
└── returns
    └── LaunchDescription Object
        └── contains
            └── launch actions
```
