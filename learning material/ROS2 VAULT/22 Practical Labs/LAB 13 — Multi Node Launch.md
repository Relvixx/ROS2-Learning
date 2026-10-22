---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 13 — Multi Node Launch

## Goal

One launch file se:

```text
publisher_node
+
subscriber_node
```

start karna.

---

# File

```text
multi_nodes.launch.py
```

Core:

```python
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

# Existing `glob()` Benefit

`setup.py` already:

```python
glob('launch/*.launch.py')
```

use karta tha.

So `multi_nodes.launch.py` ke liye separate installation rule add nahi karni padi.

---

# Build

```bash
colcon build --symlink-install --packages-select my_first_pkg
```

Installed folder showed both:

```text
parameter.launch.py
multi_nodes.launch.py
```

---

# First Multi-node Run

Launch system successfully:

```text
publisher process started ✅
subscriber process started ✅
```

but publisher later crashed with Python `NameError`.

See [[Publisher Crashed After Successful Launch]].

---

# After Fix

Launch output showed:

```text
[launch_publisher]: Hello from ROS2
[launch_subscriber]: Hello from ROS2
```

So multi-node launch + communication successfully worked.
