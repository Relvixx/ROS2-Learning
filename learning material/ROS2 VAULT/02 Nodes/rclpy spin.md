---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `rclpy.spin()`

## Ye Node chapter ka heart kyun tha?

ROS programs event-driven hote hain.

Future me Node ke andar:

- Timer callback
- Subscriber callback
- Service callback
- Action callback

jaise events aa sakte hain.

In events ko process karne ke liye executor ko run hona chahiye.

Beginner API:

```python
rclpy.spin(node)
```

---

# Precise mental model

> `rclpy.spin(node)` blocking event-processing loop run karta hai jahan Executor Node ke ready callbacks/events ko service karta hai.

Historical beginner explanation:

> "Node ko alive rakhta hai."

Useful intuition hai, lekin precise refinement:

> Node object technically spin ke bina bhi exist kar sakta hai; problem ye hai ki callbacks/events service nahi honge.

---

# Flow

```text
Node Object
   ↓
rclpy.spin(node)
   ↓
Executor event loop
   ↓
wait for ready ROS work
   ↓
callback ready?
   ↓
callback execute
   ↓
wait again
```

---

# Future connections

Publisher timer:

```text
Timer ready
 ↓
Executor
 ↓
timer_callback()
```

Subscriber:

```text
Message received
 ↓
Executor
 ↓
subscriber callback
```

Service:

```text
Request received
 ↓
Executor
 ↓
service callback
```

Action:

```text
Action-related event
 ↓
Executor
 ↓
registered callback
```

---

# Important correction

Avoid:

> "Without spin Node turant delete ho jata hai."

Better:

> Without an executor being spun, callbacks normally process nahi honge. Program ka lifetime surrounding code par depend karta hai.

---

# Knowledge Boundary

## 🟢 Must know

- spin callbacks/events process karne ke liye executor loop chalata hai.
- blocking call hai.
- Publisher/Subscriber/Service/Action callbacks se connected hai.

## 🔴 Later

- MultiThreadedExecutor
- SingleThreadedExecutor internals
- wait sets
- callback groups
- scheduling internals

---

# Related

- [[Node Runtime Flow]]
- [[First Node Anatomy]]
