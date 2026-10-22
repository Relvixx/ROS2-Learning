---
type: correction
status: canonical
language: Hinglish
---

# Callback Registration does not Change a Parameter

```python
self.add_on_set_parameters_callback(
    self.parameter_callback
)
```

Meaning:

```text
register callback
```

Not:

```text
change parameter value now
```

Actual change happens when a set request arrives later.
