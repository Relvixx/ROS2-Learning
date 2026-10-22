---
type: object
status: verified
depth: must-know
language: Hinglish
---

# LaunchDescription Object

Import:

```python
from launch import LaunchDescription
```

Object creation:

```python
LaunchDescription([
    publisher,
    subscriber
])
```

---

# What it represents

> Launch system ko actions ka description/container deta hai.

Mental model:

```text
LaunchDescription Object
├── Node launch action
├── Node launch action
└── other launch actions (future)
```

---

# Who creates it?

Launch file code:

```python
generate_launch_description()
```

ke andar.

---

# Who uses it?

ROS 2 Launch System.

---

# Important

Iske andar:

```text
running ROS Node objects
```

directly stored nahi hain.

Learned multi-node example me:

```text
publisher
subscriber
```

**Node launch-action objects** the.

See [[Launch Action Node Object]].
