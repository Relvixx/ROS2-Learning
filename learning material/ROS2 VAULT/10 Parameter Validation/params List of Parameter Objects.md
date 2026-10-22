---
type: object-reasoning
status: locked
depth: must-know
language: Hinglish
---

# `params` = List of Parameter Objects

Callback:

```python
def parameter_callback(self, params):
```

`params` ek raw single value nahi.

Mental model:

```text
params
├── Parameter object 1
├── Parameter object 2
└── ...
```

---

# One item

```python
for param in params:
```

Now:

```text
param
├── name
└── value
```

Example:

```text
param.name  = "max_speed"
param.value = 3.5
```

Important:

`param.value` = proposed/requested value being inspected.

See [[Proposed Value vs Stored Value]].
