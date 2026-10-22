---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 08 — Callback Validation

Node:

```text
/parameter_validation_node
```

Initial:

```text
max_speed = 2.0
robot_mode = normal
```

---

# Valid speed

```bash
ros2 param set /parameter_validation_node max_speed 3.5
```

Actual:

```text
Set parameter successful
```

Verify:

```bash
ros2 param get /parameter_validation_node max_speed
```

Actual:

```text
Double value is: 3.5
```

---

# Invalid speed

```bash
ros2 param set /parameter_validation_node max_speed 8.0
```

Actual:

```text
Setting parameter failed: max_speed must be between 0.0 and 5.0
```

Verify:

```text
Double value is: 3.5
```

So old valid value remained.

---

# Valid mode

```bash
ros2 param set /parameter_validation_node robot_mode safe
```

Actual:

```text
Set parameter successful
```

---

# Invalid mode

```bash
ros2 param set /parameter_validation_node robot_mode turbo
```

Actual:

```text
Setting parameter failed: robot_mode must be safe, normal, or sport
```

---

# Evidence

```text
Request made
 ↓
callback executed
 ↓
custom reason returned on failure
 ↓
CLI displayed same reason
```

This proves end-to-end callback validation.
