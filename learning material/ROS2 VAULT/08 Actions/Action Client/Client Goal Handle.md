---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Client Goal Handle

Client:

```python
goal_handle = future.result()
```

Yahan `future` completed `send_goal_future` hai.

Returned object client side par goal request / accepted goal ko represent karne wala Goal Handle hai.

---

# Important properties/methods studied

```text
goal_handle
├── accepted
└── get_result_async()
```

---

# Acceptance

```python
goal_handle.accepted
```

batata hai Goal accept hua ya reject.

---

# Result Request

Accepted goal ke baad:

```python
get_result_future = goal_handle.get_result_async()
```

---

# Server Goal Handle se difference

Server callback ka:

```python
goal_handle.request.order
goal_handle.publish_feedback(...)
goal_handle.succeed()
```

server-side execution management ke liye tha.

Client Goal Handle:

```python
accepted
get_result_async()
```

client-side accepted goal relationship ke liye.

Same variable name dekhkar same object role assume mat karo.

See [[Server Goal Handle]].
