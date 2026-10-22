---
type: comparison
status: verified
language: Hinglish
---

# Launch File vs Node

## Launch File

```text
system start/configuration/orchestration
```

## Node

```text
actual computational ROS participant
```

---

# Example

Launch file:

```python
Node(
    package='my_first_pkg',
    executable='publisher_node',
    name='launch_publisher'
)
```

Ye Publisher logic implement nahi kar raha.

Actual publisher logic:

```text
publisher_node.py
→ PublisherNode
→ Publisher Object
→ Timer
→ Message
→ /hello_topic
```

---

# Rule

> **Launch action executable ko start karne ki instruction hai; actual work launched program/node karta hai.**
