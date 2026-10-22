---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Topic Name + Message Type + QoS

Same Topic name dekhkar automatically assume mat karo ki communication guaranteed hai.

Learning mental model:

```text
Topic Name
    +
Message Type
    +
QoS Compatibility
    ↓
Communication relationship
```

---

# Topic name

Example:

```text
/hello_topic
```

Publisher aur Subscriber ko matching communication channel identify karna hota hai.

---

# Message type

Actual practical:

```text
std_msgs/msg/String
```

Python:

```python
from std_msgs.msg import String
```

Agar one side expected type compatible nahi, communication expected form me nahi hoga.

---

# QoS

Publisher aur Subscriber QoS policies ko compatible hona chahiye.

Exact same values hona universal rule nahi.

See [[QoS Fundamentals]].

---

# CLI proof

Actual:

```bash
ros2 topic type /hello_topic
```

Output:

```text
std_msgs/msg/String
```

And:

```bash
ros2 topic info /hello_topic
```

Output included:

```text
Publisher count: 1
Subscription count: 1
```

See [[LAB 03 — Topic CLI Inspection]].

---

# Related

- [[Topic Mental Model]]
- [[QoS Fundamentals]]
- [[Topic Debugging Flow]]
