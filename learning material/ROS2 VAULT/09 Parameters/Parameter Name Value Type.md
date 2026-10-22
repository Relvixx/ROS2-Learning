---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Parameter Name + Value + Type

Parameter ko teen core pieces me dekho:

```text
Parameter
├── name
├── value
└── type
```

---

# Example

```python
self.declare_parameter('max_speed', 2.0)
```

Conceptually:

```text
name
→ max_speed

value
→ 2.0

type
→ double
```

---

# Name

Parameter ko identify karta hai.

```text
max_speed
```

---

# Value

Current configuration.

```text
2.0
```

Later runtime:

```text
0.8
```

---

# Type

Value ka ROS parameter type.

For `2.0` practical:

```text
Double
```

CLI proof:

```text
Double value is: 2.0
```

and later:

```text
Double value is: 0.8
```

---

# Related

- [[Parameter Types]]
- [[declare_parameter]]
