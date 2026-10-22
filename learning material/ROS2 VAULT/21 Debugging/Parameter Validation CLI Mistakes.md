---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Parameter Validation CLI Mistakes

Two useful mistakes actual practical me aaye.

---

# 1. Wrong parameter name

Command:

```bash
ros2 param get /parameter_validation_node robot_node
```

Actual:

```text
Parameter not set
```

Declared parameter:

```text
robot_mode
```

not:

```text
robot_node
```

---

# 2. Missing set value

Command:

```bash
ros2 param set /parameter_validation_node max_speed
```

CLI error:

```text
the following arguments are required: value
```

---

# Engineering distinction

```text
CLI syntax/input error
→ valid parameter-set request bani hi nahi
→ callback tak nahi pahunchi

Validation rejection
→ request bani
→ callback executed
→ callback rejected
```
