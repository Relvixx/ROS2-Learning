---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `publish_feedback()`

Server:

```python
goal_handle.publish_feedback(feedback_msg)
```

Meaning:

> Current Action execution ka intermediate Feedback client ko publish/send karo.

---

# Why loop ke andar?

Fibonacci task progress gradually change hoti hai:

```text
[0,1]
[0,1,1]
[0,1,1,2]
...
```

Har meaningful progress step ke baad feedback publish kiya gaya.

---

# Runtime

```text
Server execution
 ↓
Feedback Object update
 ↓
publish_feedback()
 ↓
Action feedback transport
 ↓
Client registered feedback callback
 ↓
partial_sequence read
```

---

# Important

Feedback:

❌ final Result nahi  
❌ Goal state success mark nahi karta

Feedback sirf progress data hai.

---

# Related
- [[Feedback Object]]
- [[Action Feedback Callback]]
