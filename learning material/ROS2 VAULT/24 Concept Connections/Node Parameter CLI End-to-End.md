---
type: connection-map
status: verified
language: Hinglish
---

# Node → Parameter → CLI End-to-End

Batch 05 master map.

---

# Code

```python
self.declare_parameter('max_speed', 2.0)
```

Creates/declares:

```text
Node
└── max_speed
      ├── value = 2.0
      └── type = double
```

---

# Read in Python

```python
self.get_parameter('max_speed').value
```

```text
Node
 ↓
get_parameter()
 ↓
Parameter Object
 ↓
.value
 ↓
2.0
```

---

# Inspect from CLI

```bash
ros2 param get /parameter_node max_speed
```

Output:

```text
Double value is: 2.0
```

---

# Change

```bash
ros2 param set /parameter_node max_speed 0.8
```

```text
CLI
 ↓
Node parameter system
 ↓
max_speed
2.0 → 0.8
```

---

# Verify

```bash
ros2 param get /parameter_node max_speed
```

```text
Double value is: 0.8
```

---

# Configuration Connection

```text
Code default
     ↓
startup override possible
     ↓
running Node
     ↓
runtime CLI set possible
```

---

# Next Engineering Question

```text
"What values should be allowed?"
```

That begins:

[[Callbacks and Validation — Boundary Note]]
