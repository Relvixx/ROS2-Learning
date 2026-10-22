---
type: object-reasoning
status: verified
depth: must-know
language: Hinglish
---

# Parameter Object vs Parameter Value

Ye distinction object reasoning ke liye important hai.

---

# Parameter Object

```python
parameter = self.get_parameter('max_speed')
```

Conceptually:

```text
parameter
└── Parameter Object
      ├── name
      ├── value
      └── type information
```

---

# Actual Value

```python
parameter.value
```

Example:

```text
2.0
```

---

# One-line chain

```text
get_parameter()
→ Parameter Object

Parameter Object.value
→ actual current value
```

---

# Do not confuse

```text
Parameter Object
≠
2.0
```

Object contains/represents parameter data; `2.0` is one value.
