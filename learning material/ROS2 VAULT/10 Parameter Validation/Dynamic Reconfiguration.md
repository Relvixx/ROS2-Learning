---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Dynamic Reconfiguration

Parameter value change hona alone enough nahi.

Real engineering meaning:

```text
parameter changes
 ↓
running node new value read/use karta hai
 ↓
behavior/output changes
 ↓
NO restart
```

---

# Practical Node

Timer callback every 2 sec:

```python
self.timer = self.create_timer(
    2.0,
    self.control_loop
)
```

Inside:

```python
max_speed = self.get_parameter(
    'max_speed'
).value

robot_mode = self.get_parameter(
    'robot_mode'
).value
```

---

# Actual Runtime

Initially:

```text
Robot mode: normal | Max speed: 2.0
```

CLI changed speed.

Without restart:

```text
Robot mode: normal | Max speed: 4.0
```

Then mode changed:

```text
Robot mode: sport | Max speed: 4.0
```

This practically proved dynamic reconfiguration.

---

# Anti-example

Parameter changes:

```text
2.0 → 4.0
```

but code still:

```python
motor_speed = 2.0
```

Then actual behavior does **not** dynamically change.
