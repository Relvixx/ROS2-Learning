---
type: connection-map
status: verified
depth: must-know
language: Hinglish
---

# Parameter Configuration Paths

Same parameter ko different stages par value mil sakti hai.

---

# 1. Code Default

```python
self.declare_parameter('max_speed', 2.0)
```

```text
default = 2.0
```

---

# 2. Startup / Launch-provided Value

Later launch learning me:

```python
parameters=[
    {'max_speed': 0.8}
]
```

Node startup value override kar sakta hai.

```text
code default = 2.0
      ↓
launch says = 0.8
      ↓
running initial value = 0.8
```

This does not permanently rewrite source code.

See [[Launch-Time Parameter Override]].

---

# 3. Runtime Change

```bash
ros2 param set /parameter_node max_speed 0.8
```

running parameter value change.

---

# Master Map

```text
Code Default
     │
     ├──── startup override ───→ Initial Running Value
     │
     └─────────────────────────→ Initial Running Value
                                      ↓
                               Runtime CLI Set
                                      ↓
                               Current Value
```

---

# Important

`default`, `startup configured value`, aur `current runtime value` same concept nahi.
