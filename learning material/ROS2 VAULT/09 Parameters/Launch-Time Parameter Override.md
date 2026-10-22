---
type: connection
status: verified-later
depth: must-know
language: Hinglish
---

# Launch-Time Parameter Override

Parameters course scope me launch-time configuration concept included tha.

Actual launch syntax later Launch Files chapter me deeply/practically verify hua.

---

# Node default

```python
self.declare_parameter('max_speed', 2.0)
```

Default:

```text
2.0
```

---

# Later launch configuration

```python
Node(
    package='my_first_pkg',
    executable='parameter_node',
    name='config_node',
    parameters=[
        {'max_speed': 0.8}
    ]
)
```

---

# Runtime

```text
Source code default
2.0
 ↓
Launch configuration
0.8
 ↓
Node starts
 ↓
current initial max_speed = 0.8
```

---

# Important

Launch does NOT modify:

```python
self.declare_parameter('max_speed', 2.0)
```

inside source code.

A normal later run without override can again use:

```text
2.0
```

---

# Chronology

```text
Parameters chapter
→ launch-time override concept learned

Launch Files chapter
→ actual Node(... parameters=[...]) practical verified
```

So this note is cross-chapter evidence, not proof that Launch Files were already learned during basic Parameters.
