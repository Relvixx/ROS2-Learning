---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Parameter Callback Reference vs Invocation

Correct registration:

```python
self.parameter_callback
```

= method reference.

Wrong for registration intent:

```python
self.parameter_callback()
```

= method ko abhi execute karo.

---

# Same old pattern

Timer:

```python
self.create_timer(1.0, self.timer_callback)
```

Subscriber:

```python
self.create_subscription(..., self.callback, ...)
```

Parameter validation:

```python
self.add_on_set_parameters_callback(
    self.parameter_callback
)
```

Common rule:

```text
callback
→ later call karna

callback()
→ abhi call karo
```
