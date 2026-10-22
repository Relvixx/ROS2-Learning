---
type: correction
status: canonical
language: Hinglish
---

# Do not Invent a Callback Registration Handle

Historical learning me ek mistaken explanation diya gaya tha:

```python
self.param_callback_handle = self.add_on_set_parameters_callback(...)
```

aur returned handle ko important bataya gaya.

Ye later explicitly corrected hua.

---

# Canonical Model

```python
self.add_on_set_parameters_callback(
    self.parameter_callback
)
```

Focus:

```text
Node method
 ↓
callback reference register
 ↓
future set request
 ↓
callback invoked
```

Returned handle ko current learned pattern ka core concept mat banao.
