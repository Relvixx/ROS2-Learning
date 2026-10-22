---
type: runtime
status: locked
depth: must-know
language: Hinglish
---

# Action Server `execute_callback`

Core pattern:

```python
def execute_callback(self, goal_handle):
    self.get_logger().info('Executing goal...')

    order = goal_handle.request.order

    feedback_msg = Fibonacci.Feedback()
    feedback_msg.partial_sequence = [0, 1]

    for i in range(1, order):
        feedback_msg.partial_sequence.append(
            feedback_msg.partial_sequence[i] +
            feedback_msg.partial_sequence[i - 1]
        )

        goal_handle.publish_feedback(feedback_msg)

    goal_handle.succeed()

    result = Fibonacci.Result()
    result.sequence = feedback_msg.partial_sequence
    return result
```

---

# Story

```text
Goal already accepted/executing
 ↓
Server Goal Handle callback ko milta hai
 ↓
Goal request se order read
 ↓
Feedback Object create
 ↓
Fibonacci calculate
 ↓
har step Feedback publish
 ↓
task complete
 ↓
goal_handle.succeed()
 ↓
Result Object create/fill
 ↓
return result
```

---

# Important

`goal_handle` Goal Object nahi.

Ye runtime handle hai jiske through server:

- request access karta hai
- feedback publish karta hai
- goal state success mark karta hai

See [[Server Goal Handle]].
