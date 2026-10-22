---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Launch File Not Found in Share Directory

## Symptom

```bash
ros2 launch my_first_pkg parameter.launch.py
```

Error:

```text
file 'parameter.launch.py' was not found in the share directory of package 'my_first_pkg'
```

---

# Important Evidence

Package itself mil raha tha:

```text
my_first_pkg share directory found ✅
```

But launch file installed share me missing.

---

# Debugging

Source:

```bash
ls -l src/my_first_pkg/launch/
```

Source file existed ✅

`setup.py`:

```text
launch data_files entry existed ✅
```

Installed directory:

```text
install/my_first_pkg/share/my_first_pkg/launch/
```

missing ❌

---

# Root Cause

Launch file/config add hone ke baad latest package rebuild/install nahi hua tha.

---

# Fix

```bash
cd ~/ros2_jazzy

colcon build \
  --symlink-install \
  --packages-select my_first_pkg
```

Then source:

```bash
source /opt/ros/jazzy/setup.zsh
source ~/ros2_jazzy/install/setup.zsh
```

Then installed file appeared.

---

# Engineering Flow

```text
Source file exists?
 ↓
setup.py install rule exists?
 ↓
package rebuilt?
 ↓
installed share file exists?
 ↓
workspace sourced?
 ↓
ros2 launch
```

Random launch-code edits se better evidence-driven debugging.
