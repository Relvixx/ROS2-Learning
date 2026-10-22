---
type: connection-map
status: locked
language: Hinglish
---

# Fibonacci Action — End-to-End

Batch 04 ka master map.

---

# Interface

```text
Fibonacci.action

Goal
└── order

Result
└── sequence

Feedback
└── partial_sequence
```

---

# Client

```text
ActionClient Object
 ↓
Goal Object
order = 5
 ↓
send_goal_async()
 ↓
send_goal_future
```

---

# Goal Response

```text
Server responds
 ↓
send_goal_future completes
 ↓
goal_response_callback()
 ↓
Client Goal Handle
 ↓
accepted?
```

---

# Server

```text
Server Goal Handle
 ↓
request.order
 ↓
execute Fibonacci
 ↓
Feedback Object
 ↓
publish_feedback()
```

---

# Feedback Client

```text
Feedback transport
 ↓
feedback_callback(feedback_msg)
 ↓
feedback_msg.feedback
 ↓
partial_sequence
```

---

# Result Setup

Client accepted handle:

```text
get_result_async()
 ↓
get_result_future
```

---

# Server Completion

```text
task complete
 ↓
succeed()
 ↓
Fibonacci.Result()
 ↓
result.sequence
 ↓
return result
```

---

# Client Final Extraction

```text
get_result_future completes
 ↓
get_result_callback()
 ↓
future.result()
 ↓
wrapper
 ↓
.result
 ↓
Action Result Object
 ↓
sequence
```

---

# Complete Compact Timeline

```text
GOAL
 Client → Server

GOAL RESPONSE
 Server → Client Goal Handle

FEEDBACK
 Server → Client callback
 Server → Client callback
 Server → Client callback

FINAL RESULT
 Server → get_result_future → Client Result Object
```

---

# Reused Service Concepts

```text
Future
callback
async operation
interface-generated objects
spin/event processing
```

Action adds:

```text
Goal
Goal acceptance
Feedback
Goal Handle
Final Result stage
```
