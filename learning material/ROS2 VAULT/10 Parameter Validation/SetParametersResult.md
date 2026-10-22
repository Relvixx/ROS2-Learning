---
type: object
status: locked
depth: must-know
language: Hinglish
---

# `SetParametersResult`

Import:

```python
from rcl_interfaces.msg import SetParametersResult
```

Callback ko ROS 2 ko formally decision return karna hota hai.

---

# Accept

```python
return SetParametersResult(
    successful=True
)
```

---

# Reject

```python
return SetParametersResult(
    successful=False,
    reason='max_speed must be between 0.0 and 5.0'
)
```

---

# Mental Object

```text
SetParametersResult
├── successful → True / False
└── reason     → human-readable explanation
```

---

# Important Distinction

```text
Parameter Object
→ proposed parameter data

SetParametersResult
→ validation decision
```

Actual CLI me `reason` string surfaced, proving the decision path end-to-end.
