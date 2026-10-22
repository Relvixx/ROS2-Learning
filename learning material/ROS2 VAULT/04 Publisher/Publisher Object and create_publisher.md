---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Publisher Object and `create_publisher()`

Learning me yahan OOP + ROS ka important connection clear hua.

---

# Core line

```python
self.publisher_ = self.create_publisher(
    String,
    "chatter",
    10
)
```

---

# `create_publisher()` kya hai?

✅ **Method**

❌ Class nahi.

Ye `Node` class se available method hai.

Conceptual structure:

```text
Node Class
├── create_publisher()
├── create_subscription()
├── create_timer()
├── get_logger()
└── ...
```

Humari custom Node class `Node` se inherit karti hai, isliye ye methods use kar sakti hai.

---

# Method kya return karta hai?

```python
self.create_publisher(...)
```

returns:

> **Publisher Object**

Fir us reference ko store kiya:

```python
self.publisher_
```

Object tree:

```text
Current Node Object
│
├── publisher_
│      ↓
│   Publisher Object
│
└── ...
```

---

# Method vs Class — clean distinction

Simplified pseudo-code jo learning me use hua:

```python
class Node:

    def create_publisher(self, msg_type, topic, qos):
        publisher = Publisher(
            msg_type,
            topic,
            qos
        )
        return publisher
```

Yahan:

```text
create_publisher()
→ method

Publisher
→ class

Publisher(...)
→ object creation

self.publisher_
→ returned object ka reference
```

Ye pseudo-code conceptual understanding ke liye hai, real `rclpy` source implementation nahi.

---

# Arguments

```python
String
```

→ ROS message type/class

```python
"chatter"
```

→ Topic name

```python
10
```

→ shorthand QoS depth style argument in this learning example

Later correction:
`10` ko "permanently exactly 10 messages store" mat samjho.

See [[QoS Fundamentals]].

---

# `self.publisher_` me `self` kyun?

Publisher Object current Node ke saath attribute ke form me store hota hai.

```text
self
 ↓
current Node object
 ↓
publisher_
 ↓
Publisher Object
```

---

# Related

- [[self]]
- [[Why Publisher Exists]]
- [[QoS Fundamentals]]
