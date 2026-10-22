---
type: correction
status: canonical
language: Hinglish
---

# Default Value vs Runtime Value vs Launch Value

These are different.

---

# Default

```python
declare_parameter('max_speed', 2.0)
```

```text
2.0
```

---

# Launch/startup override

Later verified:

```python
parameters=[
    {'max_speed': 0.8}
]
```

Running initial value can become:

```text
0.8
```

without source default changing.

---

# Runtime CLI

```bash
ros2 param set ... max_speed 0.8
```

changes current running parameter value.

---

# Mental Model

```text
SOURCE DEFAULT
      ↓
startup configuration may override
      ↓
INITIAL RUNTIME VALUE
      ↓
runtime set may change
      ↓
CURRENT RUNTIME VALUE
```
