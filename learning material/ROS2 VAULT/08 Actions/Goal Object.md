---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Goal Object

Client task request ko Action Goal Object me prepare karta hai.

---

# Create

```python
goal_msg = Fibonacci.Goal()
```

Now:

```text
goal_msg
└── order = ?
```

---

# Fill

```python
goal_msg.order = order
```

Example:

```text
order = 5
```

Then:

```text
goal_msg
└── order = 5
```

---

# Send

```python
send_goal_future = self._action_client.send_goal_async(
    goal_msg,
    feedback_callback=self.feedback_callback
)
```

Goal Object Action Server ki taraf send/initiate hota hai.

---

# Goal ≠ Goal Handle

Goal Object:

```text
What task is requested?
```

Goal Handle:

```text
Accepted/existing goal ko represent/manage karne wala runtime object
```

See [[Goal is not Goal Handle]].
