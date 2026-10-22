---
type: concept
status: covered
depth: medium
language: Hinglish
---

# Parameter Types

Parameters lecture scope me ye categories covered the:

```text
string
integer
double
bool
arrays
```

---

# Examples mental model

```text
robot_mode = "normal"
→ string

max_count = 10
→ integer

max_speed = 2.0
→ double

enabled = true
→ bool
```

Array types bhi parameter system ka part hain.

---

# Actual practical type

`max_speed`:

```text
double
```

CLI:

```text
Double value is: 2.0
```

---

# Why type matters?

Configuration sirf naam + value nahi.

ROS ko value ka type bhi pata hota hai.

Later validation/descriptors me type/constraints aur important honge.
