---
type: dev-workflow
status: verified
depth: must-know
language: Hinglish
---

# Installing Launch Files with `setup.py`

Python package me `launch/` folder me file create kar dena enough nahi.

`ros2 launch` installed package share space se file locate karta hai.

---

# Imports

```python
import os
from glob import glob
```

---

# `data_files` Entry

```python
(
    os.path.join(
        'share',
        package_name,
        'launch'
    ),
    glob('launch/*.launch.py')
),
```

---

# Meaning

```text
glob(...)
→ source launch files

os.path.join(...)
→ install destination
```

Rahul ne correctly identify kiya tha:

```text
destination = os.path.join(...)
source      = glob(...)
```

---

# Flow

```text
src/my_first_pkg/launch/
        ↓
setup.py data_files
        ↓
colcon build/install
        ↓
install/my_first_pkg/share/my_first_pkg/launch/
        ↓
ros2 launch can find file
```

See [[glob for Launch Files]] and [[os.path.join for Launch Destination]].
