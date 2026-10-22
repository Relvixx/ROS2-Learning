---
type: code-anatomy
status: locked
depth: must-know
language: Hinglish
---

# First Node Anatomy

Historical learning code:

```python
import rclpy
from rclpy.node import Node


class SimpleNode(Node):

    def __init__(self):
        super().__init__("simple_node")
        self.get_logger().info("Hello ROS2")


def main(args=None):
    rclpy.init(args=args)

    node = SimpleNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
```

---

# Priority Map

```text
import rclpy                              🟡
from rclpy.node import Node              🟢

class SimpleNode(Node):                  🟢

def __init__(self):                      🟡
super().__init__("simple_node")          🟢
self.get_logger().info(...)              🟡

def main(args=None):                     🟡
rclpy.init(args=args)                    🟢
node = SimpleNode()                      🟢
rclpy.spin(node)                         🟢
rclpy.shutdown()                         🟡

if __name__ == "__main__":               🔵 after foundation
main()                                   🟡
```

---

# Story, syntax nahi

```text
ROS Python library import
      ↓
Node class import
      ↓
Custom SimpleNode blueprint define
      ↓
main() start
      ↓
ROS initialize
      ↓
SimpleNode object create
      ↓
spin / events process
      ↓
shutdown
```

---

# Imports

```python
import rclpy
```

ROS 2 Python client library.

```python
from rclpy.node import Node
```

Base Node class.

---

# Custom class

```python
class SimpleNode(Node):
```

Meaning:

> `SimpleNode` ROS `Node` class se inherit karti hai.

See [[Inheritance and super]].

---

# Constructor

```python
def __init__(self):
```

Object create hone par initialization path ka part.

```python
super().__init__("simple_node")
```

Base ROS Node initialize.

---

# Logger

```python
self.get_logger().info("Hello ROS2")
```

ROS logger use karke info message.

Is line ka internal logging implementation abhi needed nahi tha.

---

# Main

```python
rclpy.init(args=args)
```

ROS Python client environment initialize.

```python
node = SimpleNode()
```

Actual Node object.

```python
rclpy.spin(node)
```

Executor event processing loop ko run karne ka beginner API path.

```python
rclpy.shutdown()
```

ROS context shutdown.

---

# Connections

- [[rclpy init]]
- [[rclpy spin]]
- [[Node Runtime Flow]]
- [[main Function]]
- [[__name__ and __main__]]
