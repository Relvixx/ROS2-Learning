---
type: correction
status: canonical
language: Hinglish
---

# Source Launch File Existing ≠ ROS Can Launch It

Wrong assumption:

```text
src/.../launch/parameter.launch.py exists
→ ros2 launch must find it
```

❌

Python package workflow me learned path:

```text
source file
 ↓
setup.py data_files
 ↓
build/install
 ↓
installed share directory
 ↓
workspace source
 ↓
ros2 launch
```

Actual missing-file incident proved this.
