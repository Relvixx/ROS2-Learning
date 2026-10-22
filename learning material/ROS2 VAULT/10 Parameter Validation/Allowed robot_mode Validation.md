---
type: code-pattern
status: locked
depth: must-know
language: Hinglish
---

# Allowed `robot_mode` Validation

Allowed:

```text
safe
normal
sport
```

Code:

```python
if param.name == 'robot_mode':
    if param.value not in [
        'safe',
        'normal',
        'sport'
    ]:
        return SetParametersResult(
            successful=False,
            reason='robot_mode must be safe, normal, or sport'
        )
```

---

# `not in`

```text
"safe" not in [...]
→ False
→ don't reject

"turbo" not in [...]
→ True
→ reject
```

Actual practical:

```text
safe  → accepted
turbo → rejected
```
