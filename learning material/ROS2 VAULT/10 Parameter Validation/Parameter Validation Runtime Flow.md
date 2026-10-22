---
type: runtime-flow
status: locked
depth: must-know
language: Hinglish
---

# Parameter Validation Runtime Flow

```text
CLI
ros2 param set
        ↓
Parameter set request
        ↓
/parameter_validation_node
        ↓
registered parameter_callback(params)
        ↓
params[]
        ↓
Parameter Object
├── name
└── proposed value
        ↓
validation
        ↓
SetParametersResult
   ├── successful=True
   │       ↓
   │    value stored
   │       ↓
   │    parameter event
   │       ↓
   │    runtime code can read new value
   │
   └── successful=False
           ↓
        reject
           ↓
        old value remains
           ↓
        no changed event
```

This is Batch 06 ka master flow.
