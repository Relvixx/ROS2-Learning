---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `ParameterDescriptor`

Mental model:

```text
Parameter
├── name
├── value
└── descriptor
    ├── description
    └── declared constraints
```

---

# Role

Descriptor parameter ke baare me metadata aur supported declared constraints carry kar sakta hai.

Learning example me numeric range constraint use ki gayi.

---

# Example

```python
acceleration_descriptor = ParameterDescriptor(
    description='Allowed robot acceleration from 0.0 to 2.0',
    floating_point_range=[acceleration_range]
)
```

Then:

```python
self.declare_parameter(
    'acceleration',
    1.0,
    acceleration_descriptor
)
```

---

# Important

Descriptor aur custom callback same mechanism nahi.

See [[Callback vs Descriptor]].
