---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# ROS 2 Node Mental Model

## Canonical definition

A Node is a **computational unit in ROS 2**.

Python/rclpy me learning pattern:

```python
class MyNode(Node):
    def __init__(self):
        super().__init__("my_node")

node = MyNode()
```

---

# OOP connection

```text
Node
 ↓ parent class

MyNode
 ↓ custom class / blueprint

MyNode()
 ↓ object creation

node
 ↓ actual object reference
```

---

# Node kya own/create kar sakta hai?

```text
Node
├── Publisher
├── Subscription
├── Timer
├── Service Server
├── Service Client
├── Action Server
├── Action Client
└── Parameters
```

Future chapters me ye sab isi Node foundation par build hue.

---

# Node name

```python
super().__init__("my_node")
```

Yahan `"my_node"` ROS graph me Node ka naam set karta hai.

---

# Node and ROS Graph

Node ROS graph ka participant hai.

CLI future me Node ko inspect kar sakti hai:

```bash
ros2 node list
ros2 node info /node_name
```

---

# Node ≠ Process

Ye important refinement hai.

Beginner explanation me kabhi Node ko "independent program/process" kaha gaya tha.

Precise model:

> Node logically computational participant hai. Ek OS process me ek Node ho sakta hai, lekin multiple Nodes bhi ho sakte hain.

See [[Node is not necessarily a Process]].

---

# Node and spin

Node object exist kar sakta hai, lekin callbacks/events ko service karne ke liye executor processing required hoti hai.

Beginner rclpy pattern:

```python
rclpy.spin(node)
```

See [[rclpy spin]].

---

# One-line recall

> **Node = ROS 2 ka computational participant object jo ek responsibility perform karta hai aur communication/resources own kar sakta hai.**
