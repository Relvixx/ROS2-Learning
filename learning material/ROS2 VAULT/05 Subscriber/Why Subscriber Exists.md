---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Why Subscriber Exists

Publisher Topic par messages bhejta hai.

Ab kisi Node ko wo messages **receive/process** karne hain.

Yahin Subscriber ka role aata hai.

---

# Mental model

```text
Publisher
   ↓
Topic
   ↓
Subscriber
   ↓
Callback
   ↓
Process received Message Object
```

---

# Subscriber actively messages search karta hai?

Nahi.

Learning me ye correction explicitly clear hua:

> Subscriber manually polling/search nahi karta. ROS communication framework matching message delivery handle karta hai aur callback ko received message ke saath invoke karta hai.

---

# Example

```text
Publisher
   ↓
/chatter
   ↓
Subscriber
   ↓
callback(msg)
   ↓
msg.data
```

---

# Related

- [[Subscription Object and create_subscription]]
- [[Subscriber Callback]]
- [[Topic Mental Model]]
