---
type: correction
status: canonical
language: Hinglish
---

# Changing Parameter Value does not Automatically Change Behavior

CLI:

```bash
ros2 param set /parameter_node max_speed 0.8
```

Parameter successfully becomes:

```text
0.8
```

But if robot logic:

```python
motor_speed = 2.0
```

hardcoded use kar raha hai:

```text
actual behavior still uses 2.0
```

---

# Correct

```text
Parameter changes
 ↓
Node must read/use new value
 ↓
then behavior can change
```

A parameter is configuration input, not magic automatic behavior replacement.
