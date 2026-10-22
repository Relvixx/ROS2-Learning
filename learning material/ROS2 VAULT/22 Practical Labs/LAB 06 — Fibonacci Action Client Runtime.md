---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 06 — Fibonacci Action Client Runtime

## Goal

Python Action Client + Action Server ko together run karke Goal → Feedback → Result lifecycle observe karna.

---

# Terminal 1 — Server

```bash
cd ~/ros2_jazzy
source install/setup.zsh
ros2 run my_first_pkg fibonacci_action_server
```

---

# Terminal 2 — Client

```bash
cd ~/ros2_jazzy
source install/setup.zsh
ros2 run my_first_pkg fibonacci_action_client
```

---

# Observed successful stages before error

Historical runtime dump showed:

```text
Goal sent
 ↓
Goal accepted ✅
 ↓
Server execution
 ↓
live Fibonacci Feedback ✅
 ↓
Feedback keeps growing
```

Then an overly large requested sequence hit a ROS fixed-width integer limit.

---

# Error

Observed:

```text
OverflowError: signed integer is greater than maximum
```

Error occurred while appending value into:

```python
feedback_msg.partial_sequence.append(...)
```

Runtime then showed execute callback error and goal not reaching success state.

---

# After Fix

User confirmed:

> fix kar diya hai aur sab sahi chal raha hai

So final practical state:

```text
bug identified ✅
cause understood ✅
fix applied ✅
successful run confirmed ✅
```

Exact final post-fix terminal output was not pasted in the source, so vault does not invent it.

---

# What this practical proved

- Goal acceptance actually happened
- Feedback callback flow actually happened
- Action execution can fail mid-goal
- Interface field limits matter at runtime
- `succeed()` is only reached if execution completes successfully
- Fixing code is not enough; runtime mental model matters
