---
type: cli-reference
status: verified
depth: must-know
language: Hinglish
---

# Action CLI

---

# 1. List

```bash
ros2 action list
```

Actual observed:

```text
/fibonacci
```

Meaning:

> Action graph me `/fibonacci` available tha.

---

# 2. Info

```bash
ros2 action info /fibonacci
```

Learning goal:

- action server/client presence inspect
- connected endpoints understand

Exact output from the relevant runtime dump is not preserved cleanly enough in current source extraction to reproduce line-for-line here.

---

# 3. Interface

```bash
ros2 interface show my_first_interfaces/action/Fibonacci
```

Structure:

```text
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

---

# 4. Send Goal

```bash
ros2 action send_goal \
/fibonacci \
my_first_interfaces/action/Fibonacci \
"{order: 6}"
```

With feedback:

```bash
ros2 action send_goal \
/fibonacci \
my_first_interfaces/action/Fibonacci \
"{order: 6}" \
--feedback
```

---

# Command Breakdown

```text
/fibonacci
→ Action Name

my_first_interfaces/action/Fibonacci
→ Action Type / Interface

{order: 6}
→ Goal fields/value

--feedback
→ intermediate feedback display
```

---

# Useful CLI Flow

```text
action list
 ↓
Action exists?
 ↓
action info
 ↓
server/client?
 ↓
interface show
 ↓
Goal/Result/Feedback structure?
 ↓
send_goal --feedback
 ↓
real execution observe
```

---

# Related
- [[LAB 05 — Fibonacci Action Server and CLI]]
