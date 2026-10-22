---
type: object
status: verified
depth: must-know
language: Hinglish
---

# Launch Action Node Object

Import:

```python
from launch_ros.actions import Node
```

Create:

```python
publisher = Node(
    package='my_first_pkg',
    executable='publisher_node',
    name='launch_publisher'
)
```

---

# What is `publisher` here?

```text
publisher
→ variable/reference

Node(...)
→ launch-action object
```

It is **not**:

```text
Publisher Object
```

and not yet:

```text
actual running PublisherNode object
```

---

# Who executes it?

Launch system.

Action execute hone par target executable/process start hota hai.

---

# Core fields studied

```text
package
executable
name
parameters
```

See [[Launch package executable name]].
