---
type: code-concept
status: verified
depth: must-know
language: Hinglish
---

# `get_parameter()`

Parameter ko Node ke parameter system se retrieve/read karne ke liye:

```python
self.get_parameter('max_speed')
```

---

# Important return concept

Mental model:

```text
get_parameter('max_speed')
 ↓
Parameter Object
```

Not directly:

```text
2.0
```

---

# Value extraction pattern studied

```python
self.get_parameter('max_speed').value
```

Breakdown:

```text
self
└── get_parameter('max_speed')
      ↓
   Parameter Object
      └── value
           ↓
          2.0
```

---

# Why this distinction matters?

Same recurring ROS/Python pattern:

```text
Object
└── field / attribute
    └── actual value
```

Examples already seen:

```text
msg.data
request.a
goal_handle.request.order
```

Parameters me:

```text
parameter.value
```

---

# Related

- [[Parameter Object vs Parameter Value]]
