---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Parameter Change Request

CLI example:

```bash
ros2 param set /parameter_validation_node max_speed 3.5
```

Isko directly:

```text
"max_speed is now 3.5"
```

mat samjho.

Better:

```text
"Please change max_speed to 3.5"
```

Yani ye ek **requested/proposed value** hai.

---

# Runtime

```text
Current stored value
2.0
 ↓
CLI request
3.5
 ↓
Validation callback
 ↓
accept?
 ├── yes → stored value becomes 3.5
 └── no  → stored value remains 2.0
```

See [[Proposed Value vs Stored Value]].
