---
type: connection-map
status: locked
language: Hinglish
---

# Parameter Validation — End-to-End

```text
USER / CLI
ros2 param set
        ↓
PARAMETER SET REQUEST
        ↓
NODE
/parameter_validation_node
        ↓
REGISTERED CALLBACK
parameter_callback(params)
        ↓
params[]
        ↓
Parameter Objects
├── name
└── proposed value
        ↓
CUSTOM VALIDATION
        ↓
SetParametersResult
   ┌────────┴────────┐
   ↓                 ↓
 True              False
   ↓                 ↓
Accept             Reject
   ↓                 ↓
Stored value       Old value
changes            remains
   ↓
/parameter_events
   ↓
Timer / node behavior
reads current values
   ↓
Dynamic Reconfiguration
```

---

# Descriptor Side Path

```text
Parameter declaration
 ↓
ParameterDescriptor
 ↓
FloatingPointRange
 ↓
range enforcement
```

Practical:

```text
acceleration 1.5 ✅
acceleration 5.0 ❌
```

---

# Two Callback Types in Same Node

```text
Parameter set request
→ parameter_callback()

Timer event
→ control_loop()
```

One validates changes.

One consumes current values.
