---
type: connection
status: verified
depth: must-know
language: Hinglish
---

# Launch Parameter Override

Node code:

```python
self.declare_parameter(
    'max_speed',
    2.0
)
```

Default:

```text
2.0
```

Launch:

```python
parameters=[
    {'max_speed': 0.8}
]
```

---

# Runtime

```text
Code default
2.0
 ↓
Launch startup configuration
0.8
 ↓
Running node initial value
0.8
```

Source code default remains:

```text
2.0
```

---

# Actual Verification

```bash
ros2 param get /config_node max_speed
```

Actual:

```text
Double value is: 0.8
```

So launch-time parameter override practically verified hua.

---

# Python Structure

```python
parameters=[
    {'max_speed': 0.8}
]
```

```text
[]
→ list

{}
→ dictionary

'max_speed'
→ key

0.8
→ value
```
