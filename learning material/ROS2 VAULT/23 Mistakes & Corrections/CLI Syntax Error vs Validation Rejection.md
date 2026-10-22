---
type: correction
status: canonical
language: Hinglish
---

# CLI Syntax Error vs Validation Rejection

## Syntax error

```bash
ros2 param set /parameter_validation_node max_speed
```

Missing value.

```text
CLI rejects command
→ set request complete nahi banti
→ validation callback nahi runs
```

---

# Validation rejection

```bash
ros2 param set /parameter_validation_node max_speed 8.0
```

```text
request valid syntax
→ callback runs
→ custom rule fails
→ successful=False
→ ROS rejects requested change
```

Completely different failure stages.
