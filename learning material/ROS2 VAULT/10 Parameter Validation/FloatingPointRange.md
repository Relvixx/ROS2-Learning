---
type: object
status: locked
depth: must-know
language: Hinglish
---

# `FloatingPointRange`

Code:

```python
acceleration_range = FloatingPointRange(
    from_value=0.0,
    to_value=2.0,
    step=0.1
)
```

Object:

```text
acceleration_range
├── from_value = 0.0
├── to_value   = 2.0
└── step       = 0.1
```

Descriptor:

```python
floating_point_range=[
    acceleration_range
]
```

---

# Why `[]`?

Because `floating_point_range` field ko range objects ki sequence/list milti hai.

```text
acceleration_range
→ one object

[acceleration_range]
→ list containing that object
```

---

# Actual practical

```text
acceleration = 1.5 → accepted
acceleration = 5.0 → range rejection
```

See [[LAB 09 — Descriptor Range Validation]].
