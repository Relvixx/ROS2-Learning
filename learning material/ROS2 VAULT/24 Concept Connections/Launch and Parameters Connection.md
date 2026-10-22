---
type: connection-map
status: verified
language: Hinglish
---

# Launch and Parameters Connection

Parameters taught:

```text
Node code default
max_speed = 2.0
```

Launch adds startup configuration:

```python
parameters=[
    {'max_speed': 0.8}
]
```

Runtime:

```text
same node code
 ↓
different startup configuration
 ↓
running max_speed = 0.8
```

---

# Engineering value

```text
Code
→ reusable logic

Launch
→ deployment/startup configuration
```

Same source code different environments me different configuration ke saath start ho sakta hai.

Actual first launch practical verified this connection.
