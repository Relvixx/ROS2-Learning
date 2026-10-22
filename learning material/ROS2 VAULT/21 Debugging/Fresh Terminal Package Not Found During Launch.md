---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Fresh Terminal — Package Not Found During Launch

Observed:

```bash
ros2 launch my_first_pkg parameter.launch.py
```

Error:

```text
Package 'my_first_pkg' not found
searching: ['/opt/ros/jazzy']
```

---

# Root Cause

Fresh/current shell workspace overlay source nahi hui thi.

---

# Fix

```bash
source /opt/ros/jazzy/setup.zsh
source ~/ros2_jazzy/install/setup.zsh
```

---

# Important Distinction

```bash
cd ~/ros2_jazzy
```

only directory change.

```bash
source ~/ros2_jazzy/install/setup.zsh
```

shell environment/package discovery update.

So:

```text
cd ≠ source
```
