---
type: callback
status: locked
depth: must-know
language: Hinglish
---

# Action Feedback Callback

Registered during:

```python
send_goal_async(
    goal_msg,
    feedback_callback=self.feedback_callback
)
```

---

# Callback

```python
def feedback_callback(self, feedback_msg):

    feedback = feedback_msg.feedback

    self.get_logger().info(
        f'Feedback: {feedback.partial_sequence}'
    )
```

---

# Object Chain

```text
feedback_msg
└── feedback
    └── partial_sequence
```

---

# Important

Feedback callback:

- `goal_response_callback()` ke andar manually call nahi hota
- `get_result_future` se repeatedly retrieve nahi hota
- execution ke dauran feedback events aane par registered callback trigger hota hai

---

# Related
- [[Feedback Object]]
- [[Action Client Three Pipelines]]
