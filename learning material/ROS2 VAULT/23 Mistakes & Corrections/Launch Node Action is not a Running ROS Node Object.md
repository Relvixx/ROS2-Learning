---
type: correction
status: canonical
language: Hinglish
---

# Launch Node Action is not a Running ROS Node Object

Code:

```python
publisher = Node(
    package='my_first_pkg',
    executable='publisher_node'
)
```

Wrong:

```text
publisher = actual PublisherNode running object
```

❌

Correct:

```text
publisher
→ reference to launch_ros.actions.Node action object
```

Launch system later action execute karta hai, then target executable/process starts.

See [[Launch Action Node Object]].
