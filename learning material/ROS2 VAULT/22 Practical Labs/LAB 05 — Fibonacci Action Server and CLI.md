---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 05 — Fibonacci Action Server and CLI

## Goal

Custom Fibonacci Action Interface + Action Server ko run karke CLI se discover aur Goal send karna.

---

# Historical Implementation Architecture

Initial implementation lesson me separate interface + implementation packages use hue:

```text
my_first_interfaces
→ Action Interface

my_first_package / later current package naming evolved
→ Python implementation
```

Current learning workspace/package history later `my_first_pkg` ke saath continue hui.

---

# Interface

```text
Fibonacci.action

int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

---

# Server Start

Later current workspace practical:

```bash
cd ~/ros2_jazzy
source install/setup.zsh
ros2 run my_first_pkg fibonacci_action_server
```

---

# Discovery

Second terminal:

```bash
cd ~/ros2_jazzy
source install/setup.zsh
ros2 action list
```

Actual:

```text
/fibonacci
```

This proved Action was registered/discoverable.

---

# CLI Goal Test

Studied command:

```bash
ros2 action send_goal \
/fibonacci \
my_first_interfaces/action/Fibonacci \
"{order: 6}" \
--feedback
```

Expected learned behavior:

```text
Goal accepted
Feedback updates
Final Result
```

---

# Server-side goal field

CLI:

```text
order = 6
```

Server:

```python
order = goal_handle.request.order
```

---

# What this lab proved

```text
Custom Action Interface available
        ↓
Action Server running
        ↓
/fibonacci discoverable
        ↓
CLI can act as Action Client
        ↓
Goal reaches server
        ↓
Feedback can be observed
        ↓
Result can be returned
```

---

# Debugging connection

A later full Python client/server run produced real Feedback then failed with fixed-width integer overflow for an excessively large Fibonacci request.

See [[Action Fixed Width Integer Overflow]].
