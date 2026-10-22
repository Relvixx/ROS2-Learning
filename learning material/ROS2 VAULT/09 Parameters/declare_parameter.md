---
type: code-concept
status: verified
depth: must-know
language: Hinglish
---

# `declare_parameter()`

Core learning line:

```python
self.declare_parameter('max_speed', 2.0)
```

---

# Kya hai?

`Node` object par available method.

```text
self
 ↓
current Node object
 ↓
declare_parameter(...)
```

---

# Arguments

```text
'max_speed'
→ Parameter name

2.0
→ default value
```

---

# Runtime meaning

```text
Node initialization
 ↓
declare_parameter('max_speed', 2.0)
 ↓
Node now has a parameter named max_speed
 ↓
default value = 2.0
```

Unless startup configuration overrides it.

---

# Important

`declare_parameter()` normal local Python variable create karne jaisa nahi.

Wrong equivalence:

```python
self.declare_parameter('max_speed', 2.0)
```

=

```python
max_speed = 2.0
```

❌

ROS Parameter system me declaration additional runtime/configuration behavior provide karta hai.

See [[Parameter is not a Python Variable]].
