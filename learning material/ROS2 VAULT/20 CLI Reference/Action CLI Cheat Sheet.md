---
type: cheat-sheet
status: verified
language: Hinglish
---

# ⌨️ Action CLI Cheat Sheet

```bash
ros2 action list
```
→ available Actions

```bash
ros2 action info /fibonacci
```
→ Action server/client information

```bash
ros2 interface show my_first_interfaces/action/Fibonacci
```
→ Goal / Result / Feedback structure

```bash
ros2 action send_goal \
/fibonacci \
my_first_interfaces/action/Fibonacci \
"{order: 6}"
```
→ Goal send

```bash
ros2 action send_goal \
/fibonacci \
my_first_interfaces/action/Fibonacci \
"{order: 6}" \
--feedback
```
→ Goal + feedback observe

---

# Actual verified discovery

```text
ros2 action list
→ /fibonacci
```

See [[LAB 05 — Fibonacci Action Server and CLI]].
