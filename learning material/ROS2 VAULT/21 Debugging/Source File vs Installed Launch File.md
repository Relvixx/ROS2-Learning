---
type: debugging-model
status: verified
language: Hinglish
---

# Source File vs Installed Launch File

Launch debugging me major distinction:

```text
SOURCE
~/ros2_jazzy/src/my_first_pkg/launch/parameter.launch.py
```

vs

```text
INSTALLED PACKAGE SHARE
~/ros2_jazzy/install/my_first_pkg/share/my_first_pkg/launch/
```

---

# Why it matters

Source file exist kar sakti hai:

```text
✅
```

but if build/install not updated:

```text
installed launch file missing ❌
```

Then:

```bash
ros2 launch ...
```

file nahi find karega.

---

# Flow

```text
SOURCE
 ↓ setup.py installation rule
BUILD / INSTALL
 ↓
INSTALL SHARE
 ↓
ros2 launch discovery
```
