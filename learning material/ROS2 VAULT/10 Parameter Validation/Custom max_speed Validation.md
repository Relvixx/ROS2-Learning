---
type: code-pattern
status: locked
depth: must-know
language: Hinglish
---

# Custom `max_speed` Validation

Rule:

```text
0.0 <= max_speed <= 5.0
```

Code:

```python
if param.name == 'max_speed':
    if param.value < 0.0 or param.value > 5.0:
        return SetParametersResult(
            successful=False,
            reason='max_speed must be between 0.0 and 5.0'
        )
```

---

# Valid

```text
3.5 < 0.0 ? no
3.5 > 5.0 ? no
→ valid
```

---

# Invalid

```text
8.0 > 5.0 ? yes
→ reject
```

Actual runtime:

```text
Setting parameter failed:
max_speed must be between 0.0 and 5.0
```

See [[LAB 08 — Callback Validation]].
