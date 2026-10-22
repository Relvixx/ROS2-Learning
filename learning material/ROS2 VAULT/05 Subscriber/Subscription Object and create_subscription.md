---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Subscription Object and `create_subscription()`

Core pattern:

```python
self.subscription = self.create_subscription(
    String,
    "chatter",
    self.callback,
    10
)
```

---

# `create_subscription()` kya hai?

✅ `Node` class ka method.

❌ Class nahi.

Method ek Subscription Object return karta hai.

```text
create_subscription()
 ↓
Subscription Object
 ↓
self.subscription
```

---

# Arguments decode

## `String`

Expected ROS message type/class.

## `"chatter"`

Topic name.

## `self.callback`

Callback method ka **reference**.

Abhi callback execute nahi ho raha.

## `10`

Basic QoS/depth argument in this example.

---

# Node object relation

```text
Subscriber Node Object
│
└── subscription
       ↓
   Subscription Object
```

---

# Important compatibility idea

Sirf same Topic name enough nahi.

Communication ke liye relevant tha:

```text
Topic name
+
Message type
+
QoS compatibility
```

See [[Topic Name Message Type and QoS]].

---

# Related

- [[Subscriber Callback]]
- [[Callback Reference vs Invocation]]
- [[QoS Fundamentals]]
