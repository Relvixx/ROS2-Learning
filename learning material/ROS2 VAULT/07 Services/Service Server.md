---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Service Server

Service Server ka main role:

> Incoming Request ko process karke Response prepare karna.

---

# Conceptual Code

```python
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class AddTwoIntsServer(Node):

    def __init__(self):
        super().__init__('add_two_ints_server')

        self.service = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.callback
        )

    def callback(self, request, response):
        response.sum = request.a + request.b
        return response
```

---

# Resources

```text
Server Node Object
└── self.service
      ↓
   Service Object / handle
```

---

# Runtime

```text
Service Server Node
 ↓
create_service(...)
 ↓
service registered
 ↓
spin / event processing
 ↓
Request arrives
 ↓
callback(request, response)
 ↓
process request
 ↓
prepare response
 ↓
return response
```

---

# Related

- [[create_service]]
- [[Server Service Callback]]
- [[Service Runtime Flow]]
