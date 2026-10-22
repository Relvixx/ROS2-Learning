---
type: code-concept
status: locked
depth: must-know
language: Hinglish
---

# `add_on_set_parameters_callback()`

Code:

```python
self.add_on_set_parameters_callback(
    self.parameter_callback
)
```

---

# Meaning

```text
Node starts
 ↓
callback reference register
 ↓
ROS 2 remembers it
 ↓
future parameter set request
 ↓
ROS 2 invokes callback
```

---

# Important

Ye line:

```text
callback ko register karti hai
```

Ye line:

```text
parameter value change nahi karti
```

Actual change request later CLI ya another parameter client path se aati hai.

---

# Historical Correction

Learning ke beech ek point par is method ke returned "handle/object" ko important bataya gaya tha.

Baad me explicitly correct kiya gaya:

> Current mental model me focus **registration action** par rakho. Returned handle ko core concept mat banao.

See [[Do not Invent a Callback Registration Handle]].
