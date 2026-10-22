---
type: dev-workflow
status: observed
language: Hinglish
---

# `--symlink-install` and Launch Files

Actual installed launch listing:

```text
parameter.launch.py ->
/home/relvixx/ros2_jazzy/build/my_first_pkg/launch/parameter.launch.py
```

This was observed after:

```bash
colcon build --symlink-install --packages-select my_first_pkg
```

---

# Beginner mental model

Install space me normal independent copy ke bajay symlink/reference behavior visible tha.

Useful development intuition:

```text
source/build artifact
← linked from install location
```

Exact colcon/setuptools symlink internals current chapter ka scope nahi tha.
