---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Topic Mental Model

## Definition

> **Topic = named publish/subscribe communication channel.**

---

# Topic kya nahi hai?

Topic:

❌ Python variable nahi  
❌ Message Object nahi  
❌ Publisher Object nahi

Example:

```python
self.publisher_ = self.create_publisher(
    String,
    "chatter",
    10
)
```

Yahan:

```text
self.publisher_
→ Python attribute holding Publisher Object

"chatter"
→ ROS Topic name
```

Dono same cheez nahi.

---

# Many-to-many idea

Ek Topic par:

```text
multiple Publishers
        ↓
      Topic
        ↓
multiple Subscribers
```

ho sakte hain.

---

# Topic inherently "continuous" hai?

Nahi.

Topic pub/sub channel hai.

Data:

- periodic
- event-driven
- bursty
- sparse

kuch bhi ho sakta hai.

---

# Theory vs Practical

Theory example:

```text
/chatter
```

Actual practical:

```text
/hello_topic
```

---

# Graph mental model

```text
Publisher Node
     ↓
Publisher Object
     ↓
/hello_topic
     ↓
Subscription Object
     ↓
Subscriber Node
```

---

# Related

- [[Topic Name Message Type and QoS]]
- [[Topic CLI]]
- [[Publisher Topic Subscriber End-to-End]]
