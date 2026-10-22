---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Feedback Object

Action execution ke beech progress data.

Server side:

```python
feedback_msg = Fibonacci.Feedback()
```

Then:

```python
feedback_msg.partial_sequence = [0, 1]
```

---

# Publish

```python
goal_handle.publish_feedback(feedback_msg)
```

Current progress client tak bheja jata hai.

---

# Client side

Client receives feedback through registered:

```python
feedback_callback(feedback_msg)
```

But client callback argument me wrapper structure discussed hua:

```text
feedback_msg
└── feedback
     └── partial_sequence
```

So code:

```python
feedback = feedback_msg.feedback
feedback.partial_sequence
```

---

# Feedback ≠ Result

Feedback intermediate progress.

Result final output.

See [[Feedback is not the Final Result]].
