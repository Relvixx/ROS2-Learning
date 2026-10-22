---
type: correction
status: canonical
language: Hinglish
---

# Server and Client Goal Handles are Different Roles

Code me dono jagah variable naam:

```text
goal_handle
```

mil sakta hai.

Isliye confusion easy hai.

---

# Server Callback Handle

```python
def execute_callback(self, goal_handle):
```

Used for:

```text
request
publish_feedback()
succeed()
```

---

# Client Handle

```python
goal_handle = future.result()
```

Used for:

```text
accepted
get_result_async()
```

---

# Rule

Variable naam same dekhkar object role same assume mat karo.

Context + type/owner matter karta hai.
