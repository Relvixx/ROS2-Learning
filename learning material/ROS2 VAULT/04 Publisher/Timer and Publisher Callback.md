---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Timer and Publisher Callback

Typical publisher code:

```python
self.timer = self.create_timer(
    0.5,
    self.publish_message
)
```

---

# `create_timer()` kya hai?

`Node` ka method.

Conceptually Timer Object create/return karta hai.

```text
create_timer()
 ↓
Timer Object
 ↓
self.timer
```

---

# `0.5`

Timer period.

Learning example me:

```text
0.5 seconds
```

ke interval par callback ready hota hai.

Actual later practical publisher `/hello_topic` roughly **1 second period** use kar raha tha aur `ros2 topic hz` se ~1 Hz measure hua.

---

# Callback

```python
self.publish_message
```

ye callback **reference** hai.

ROS ko meaning:

> Timer event ready ho to is method ko call karna.

Important:

```python
self.publish_message
```

≠

```python
self.publish_message()
```

See [[Callback Reference vs Invocation]].

---

# Runtime relation with spin

```text
Node
 ↓
Timer Object
 ↓
rclpy.spin(node)
 ↓
Executor waits
 ↓
Timer ready
 ↓
publish_message callback
 ↓
Message create
 ↓
publish
```

Timer apne aap Python syntax magic se callback run nahi karta; ROS event-processing path ke through callback execute hota hai.

---

# Related

- [[rclpy spin]]
- [[Callback Reference vs Invocation]]
- [[Publisher Runtime Flow]]
