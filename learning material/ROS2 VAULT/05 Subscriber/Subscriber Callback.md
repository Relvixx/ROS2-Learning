---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Subscriber Callback

Typical:

```python
def callback(self, msg):
    self.get_logger().info(msg.data)
```

---

# Callback kab run hota hai?

`create_subscription()` ke waqt callback register hota hai.

Callback us moment execute nahi hota.

Runtime:

```text
Subscription created
 ↓
callback reference registered
 ↓
spin / event processing
 ↓
compatible message arrives
 ↓
ROS invokes callback
 ↓
callback(self, msg)
```

---

# `self`

Current Subscriber Node object.

See [[self]].

---

# `msg`

Received ROS Message Object jo ROS callback ko provide karta hai.

Subscriber manually:

```python
msg = String()
```

nahi banata received message ke liye.

See [[Received Message Object]].

---

# `msg.data`

```text
msg
 ↓
received String Message Object
 ↓
data field
```

Publisher ne field me data write kiya.

Subscriber field read karta hai.

---

# Important distinction

```python
self.callback
```

→ function/method reference

```python
self.callback()
```

→ immediate invocation

See [[Callback Reference vs Invocation]].

---

# Related

- [[Subscription Object and create_subscription]]
- [[Received Message Object]]
- [[Subscriber Runtime Flow]]
