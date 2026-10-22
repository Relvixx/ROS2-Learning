---
type: boundary
status: next-batch
language: Hinglish
---

# Callbacks and Validation — Boundary Note

Basic Parameters chapter completed:

```text
DECLARE
 ↓
READ
 ↓
CLI CHANGE
 ↓
VERIFY
```

Question that naturally follows:

> Agar koi unsafe value set kare to?

Example:

```bash
ros2 param set /parameter_node max_speed -50.0
```

Basic Parameter system understanding alone me humne acceptance/rejection rules nahi banaye.

---

# Next Chapter

```text
Parameter Change Request
 ↓
Parameter Callback
 ↓
Inspect proposed Parameter Objects
 ↓
Validate
 ↓
SetParametersResult
 ↓
ACCEPT / REJECT
```

Next batch will include:

- callbacks
- validation
- `SetParametersResult`
- callback registration
- multiple parameters
- descriptor
- range constraint
- dynamic reconfiguration
- `/parameter_events`
- real valid/invalid CLI tests

Nothing above is treated as part of Batch 05 mastery.
