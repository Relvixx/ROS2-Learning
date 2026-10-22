---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Default Parameter Value

Code:

```python
self.declare_parameter('max_speed', 2.0)
```

Here:

```text
2.0
→ default value
```

---

# Meaning

Agar koi startup override nahi diya:

```text
Node starts
 ↓
max_speed = 2.0
```

Actual basic practical me initial CLI get:

```text
Double value is: 2.0
```

---

# Default ≠ permanent value

Runtime me:

```bash
ros2 param set /parameter_node max_speed 0.8
```

ke baad running node ke parameter ki current value:

```text
0.8
```

ho gayi.

But source code ka default:

```text
2.0
```

permanently rewrite nahi hua.

---

# Later launch connection

Launch file startup par different initial value provide kar sakti hai.

See [[Launch-Time Parameter Override]].
