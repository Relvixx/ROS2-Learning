---
type: correction
status: canonical
language: Hinglish
---

# Declared Parameter ≠ Cached Local Value

Suppose:

```python
self.declare_parameter('max_speed', 2.0)

self.max_speed = 2.0
```

Now two pieces of state ho sakte hain:

```text
ROS Parameter
max_speed

and

Python attribute
self.max_speed
```

---

# Runtime problem

CLI changes:

```text
ROS Parameter
2.0 → 0.8
```

But if:

```python
self.max_speed
```

update nahi hua, it may still hold old value.

---

# Lesson

> Parameter state aur local cached state ko automatically identical assume mat karo.

Next validation/dynamic-reconfiguration chapter me ye relationship aur important hota hai.
