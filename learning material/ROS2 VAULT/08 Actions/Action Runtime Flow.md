---
type: runtime-flow
status: locked
depth: must-know
language: Hinglish
---

# Action Runtime Flow

Example:

```python
action_client.send_goal(5)
```

---

# 1. Client Setup

```text
rclpy.init()
 ↓
FibonacciActionClient()
 ↓
ActionClient(self, Fibonacci, 'fibonacci')
```

Abhi Goal send nahi.

---

# 2. Goal Build

```text
send_goal(5)
 ↓
Fibonacci.Goal()
 ↓
goal_msg.order = 5
```

---

# 3. Goal Request

```text
send_goal_async(goal_msg, feedback_callback=...)
 ↓
send_goal_future
```

Feedback callback bhi register.

---

# 4. Goal Response

Server goal request handle karta hai.

```text
send_goal_future completes
 ↓
goal_response_callback()
 ↓
future.result()
 ↓
Client Goal Handle
 ↓
accepted?
```

---

# 5. Server Execution

Server execute callback:

```text
Server Goal Handle
 ↓
goal_handle.request.order
 ↓
5
 ↓
calculate Fibonacci
```

---

# 6. Feedback

Server:

```text
partial_sequence = [0,1]
 ↓
publish_feedback()
```

Client:

```text
feedback_callback()
 ↓
feedback_msg.feedback.partial_sequence
```

Repeat multiple times.

---

# 7. Result Future

Accepted Client Goal Handle:

```text
get_result_async()
 ↓
get_result_future
```

Pending while task executes.

---

# 8. Task Completion

Server:

```text
processing complete
 ↓
goal_handle.succeed()
 ↓
Result Object prepare
 ↓
return result
```

---

# 9. Final Result

Client:

```text
get_result_future completes
 ↓
get_result_callback()
 ↓
future.result().result
 ↓
result.sequence
```

---

# Master Timeline

```text
CLIENT                               SERVER

Goal Object
   │
   │──────── Goal request ────────────→│
   │                                   │
send_goal_future                      │
   │                                   │
   │←──── goal response ───────────────│
   ↓
Client Goal Handle
   │
   ├── accepted
   └── get_result_async()
        ↓
   get_result_future                   │
        │                              │
        │←──── Feedback ───────────────│
        │←──── Feedback ───────────────│
        │←──── Feedback ───────────────│
        │                              │
        │                         succeed()
        │                              │
        │←──── Final Result ───────────│
        ↓
future.result().result
        ↓
Result Object
```
