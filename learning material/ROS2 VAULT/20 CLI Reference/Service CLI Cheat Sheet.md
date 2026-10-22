---
type: cheat-sheet
status: verified
language: Hinglish
---

# ⌨️ Service CLI Cheat Sheet

```bash
ros2 service list
```
→ available Services

```bash
ros2 service type /add_two_ints
```
→ Service type/interface

```bash
ros2 service info /add_two_ints
```
→ client/server endpoint counts + type

```bash
ros2 service call /add_two_ints \
example_interfaces/srv/AddTwoInts \
"{a: 5, b: 7}"
```
→ manual Request

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```
→ Request/Response structure

---

# Actual verified values

```text
Service: /add_two_ints
Type: example_interfaces/srv/AddTwoInts

Request:
a=5
b=7

Response:
sum=12
```

See [[LAB 04 — AddTwoInts Service CLI]].
