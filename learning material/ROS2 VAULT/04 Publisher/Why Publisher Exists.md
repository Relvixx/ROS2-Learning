---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Why Publisher Exists

Node chapter me humare paas ek Node tha jo logger ke through terminal par message dikha sakta tha.

Lekin robot system me ek Node ko doosre Node tak **data bhejna** hota hai.

Yahin Publisher ki zarurat aati hai.

---

# Simple definition

> **Publisher ka kaam data ko ek ROS Topic par publish karna hota hai.**

Example mental model:

```text
Camera Node
   ↓
Publisher
   ↓
/camera_image
   ↓
Other Nodes
```

---

# Publisher khud data generate karta hai?

Nahi.

Ye chapter ka important verified point tha:

```text
Message create karna
→ hum / callback

Message data fill karna
→ hum / callback

Message Topic par bhejna
→ Publisher Object
```

Example:

```python
msg = String()
msg.data = "Hello"
self.publisher_.publish(msg)
```

Breakdown:

```text
String()
→ Message Object create

msg.data = "Hello"
→ Data fill

publish(msg)
→ Publisher sends
```

---

# Publisher ko kis Topic par bhejna hai kaise pata?

Publisher create hote waqt configure hota hai:

```python
self.publisher_ = self.create_publisher(
    String,
    "chatter",
    10
)
```

Publisher Object ki lifetime ke dauran uske paas topic/type/QoS configuration associated rehti hai.

Isliye later:

```python
self.publisher_.publish(msg)
```

me Topic ka naam dobara pass nahi karna padta.

---

# Related

- [[Publisher Object and create_publisher]]
- [[ROS Message Class vs Message Object]]
- [[Publisher Runtime Flow]]
- [[Topic Mental Model]]
