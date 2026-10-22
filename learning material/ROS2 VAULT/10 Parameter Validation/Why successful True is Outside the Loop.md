---
type: reasoning
status: locked
depth: must-know
language: Hinglish
---

# Why `successful=True` is Outside the Loop

Wrong pattern:

```python
for param in params:
    if first_param_is_valid:
        return SetParametersResult(successful=True)
```

Problem:

```text
first param valid
 ↓
return True immediately
 ↓
callback ends
 ↓
second invalid param never checked
```

---

# Example

```text
max_speed = 4.0      ✅
robot_mode = turbo   ❌
```

If first item ke baad success return:

```text
turbo never validated
```

---

# Correct pattern

```python
for param in params:
    # reject when a rule fails

return SetParametersResult(
    successful=True
)
```

Meaning:

> Saare checked parameters validation pass kar gaye, tab success.
