---
type: comparison
status: verified
language: Hinglish
---

# Parameter vs Hardcoded Value

## Hardcoded

```python
max_speed = 2.0
```

Changing configuration often means code change.

---

# Parameter

```python
self.declare_parameter('max_speed', 2.0)
```

Now value ROS parameter system ka part hai.

It can be:

- inspected
- configured at startup
- changed at runtime where allowed
- dumped through CLI

---

# Important

Parameter use karna source code logic ko eliminate nahi karta.

Node ko new parameter value actually **read/use** bhi karni hoti hai.

See [[Parameter Change vs Behavior Change]].
