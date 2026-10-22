---
type: mental-model
status: locked
depth: must-know
language: Hinglish
---

# Parameter Callback Mental Model

```text
Parameter Set Request
        ↓
Registered callback runs
        ↓
params list
        ↓
Parameter Objects
        ↓
param.name / param.value
        ↓
Validation Rules
        ↓
SetParametersResult
   ┌────────┴────────┐
   ↓                 ↓
True               False
   ↓                 ↓
Accept             Reject
   ↓                 ↓
New value          Old value stays
```

---

# Callback ka role

> Parameter change ko accept/reject karne ke decision path me custom logic lagana.

Callback itself CLI command nahi.

Callback itself parameter value nahi.

Callback ek registered function/method hai jo set request ke time ROS 2 ke dwara invoke hota hai.
