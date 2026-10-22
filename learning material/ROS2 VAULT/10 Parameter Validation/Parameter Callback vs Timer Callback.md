---
type: comparison
status: locked
language: Hinglish
---

# Parameter Callback vs Timer Callback

Same Node me dono callbacks the, but trigger different.

---

# Parameter Callback

```python
parameter_callback(...)
```

Trigger:

```text
parameter set request
```

Role:

```text
validate proposed changes
```

---

# Timer Callback

```python
control_loop()
```

Trigger:

```text
timer every 2 sec
```

Role:

```text
current parameter values read/use
```

---

# Runtime

```text
CLI SET
 ↓
parameter_callback()
 ↓
accepted
 ↓
stored parameter changes

Later timer fires
 ↓
control_loop()
 ↓
get_parameter()
 ↓
new value used
```

This connection is the heart of the dynamic reconfiguration practical.
