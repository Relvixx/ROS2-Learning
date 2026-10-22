---
type: concept
status: canonical
depth: must-know
language: Hinglish
---

# ROS 2 Interface Hierarchy

Service chapter me Interface ko dubara zero se revise kiya gaya tha kyunki concept bhool gaya tha.

Simple mental model:

> **Interface ek formal data-definition / contract hai jo batata hai ROS 2 data ka structure kaisa hoga.**

Class analogy useful hai, lekin exact equality nahi:

```text
Class = Python blueprint
Interface = ROS data definition
```

ROS tools language-specific types/classes generate karte hain jinse objects bante hain.

---

# Canonical Hierarchy

```text
ROS 2 Interface
├── Message Interface (.msg)
├── Service Interface (.srv)
└── Action Interface (.action)
```

Important:

> **Interface ko Message ka synonym mat samjho.**

Message Interface interface ka ek type hai.

---

# Message Interface

Example:

```text
std_msgs/msg/String
```

Structure:

```text
string data
```

Generated Python type:

```python
from std_msgs.msg import String
```

Object:

```python
msg = String()
```

---

# Service Interface

Example:

```text
example_interfaces/srv/AddTwoInts
```

Structure:

```text
int64 a
int64 b
---
int64 sum
```

Meaning:

```text
Request
+
Response
```

See [[Service Interface]].

---

# Action Interface

Action chapter me later:

```text
Goal
+
Result
+
Feedback
```

Detailed Actions notes next vault batch me aayenge.

---

# Related

- [[ROS Message Class vs Message Object]]
- [[Service Interface]]
