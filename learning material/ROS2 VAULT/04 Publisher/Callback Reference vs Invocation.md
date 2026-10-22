---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Callback Reference vs Invocation

Ye Publisher/Subscriber learning ka bahut important Python + ROS connection tha.

---

# Reference

```python
self.publish_message
```

Meaning:

> Is method ka reference do. Abhi execute mat karo.

ROS API is reference ko register/store kar sakta hai aur event aane par later call kar sakta hai.

---

# Invocation

```python
self.publish_message()
```

Meaning:

> Method ko **abhi** execute karo.

---

# Timer example

Correct callback registration:

```python
self.create_timer(
    0.5,
    self.publish_message
)
```

Mental model:

```text
Timer
 ↓
callback reference store
 ↓
period complete
 ↓
ROS invokes callback
```

---

# Subscriber example

```python
self.create_subscription(
    String,
    "chatter",
    self.callback,
    10
)
```

`self.callback` reference hai.

Subscription create hote waqt callback execute nahi hota.

Matching message aane par ROS callback call karta hai.

---

# Golden rule

```text
callback
→ "Later call karna"

callback()
→ "Abhi call karo"
```

---

# Related

- [[Function Definition vs Invocation]]
- [[Timer and Publisher Callback]]
- [[Subscriber Callback]]
