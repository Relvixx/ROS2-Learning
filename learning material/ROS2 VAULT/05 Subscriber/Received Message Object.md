---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Received Message Object

Subscriber callback:

```python
def callback(self, msg):
    ...
```

Yahan `msg` kaha se aaya?

> ROS communication runtime received message ko callback argument ke form me provide karta hai.

---

# Publisher side

```python
message = String()
message.data = "Hello"
publisher.publish(message)
```

Publisher side par application ne Message Object create/fill kiya.

---

# Subscriber side

```python
def callback(self, msg):
    print(msg.data)
```

Subscriber callback ko received Message Object milta hai.

---

# Object flow mental model

```text
Publisher code
 ↓
String Message Object
 ↓
publish()
 ↓
Topic
 ↓
compatible Subscription
 ↓
callback(msg)
 ↓
received Message Object
 ↓
msg.data
```

---

# `msg` normal string nahi

```python
msg
```

ROS `String` Message Object hai.

```python
msg.data
```

us object ka field.

---

# Related

- [[ROS Message Class vs Message Object]]
- [[Subscriber Callback]]
- [[Publisher Topic Subscriber End-to-End]]
