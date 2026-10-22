---
type: correction
status: canonical
language: Hinglish
---

# Parameter is not a Python Variable

Wrong equivalence:

```python
self.declare_parameter('max_speed', 2.0)
```

=

```python
max_speed = 2.0
```

❌

---

# Python Variable

```python
max_speed = 2.0
```

Python program state.

---

# ROS Parameter

```python
self.declare_parameter('max_speed', 2.0)
```

Node-associated ROS configuration state.

Can be accessed through ROS parameter APIs / CLI.

---

# Correct mental model

```text
Node
└── ROS Parameter
     └── max_speed = 2.0
```

Python local variable aur ROS Parameter overlap kar sakte hain in value, but system role different hai.
