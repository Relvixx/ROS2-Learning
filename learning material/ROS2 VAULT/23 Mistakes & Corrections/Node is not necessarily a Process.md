---
type: correction
status: canonical
language: Hinglish
---

# Node is not necessarily a Process

## Historical simplified explanation

Learning ke early stage me Node ko kabhi is tarah describe kiya gaya:

> "Node ek independent program/process hai."

Beginner intuition ke liye ye useful tha, lekin technically exact nahi.

---

# Correct mental model

> **Node = ROS 2 computational unit / participant.**

Python `rclpy` me Node ek object hota hai jo `rclpy.node.Node` se derived class instantiate karke create kiya ja sakta hai.

```python
class MyNode(Node):
    ...

node = MyNode()
```

---

# Node vs Process

Operating-system process aur ROS Node different abstraction levels hain.

Possible:

```text
Process A
└── Node 1
```

Lekin also possible:

```text
Process B
├── Node 2
└── Node 3
```

So:

```text
1 Node = 1 Process
```

universal rule nahi hai.

---

# Why correction important hai?

Future topics:

- Composition
- Component Nodes
- Executors
- Multi-node processes

me ye distinction important banega.

---

# What to remember now

🟢 Node = computational ROS participant  
🟢 Process = operating-system execution container  
🟢 Often beginner projects me one executable/process → one Node dikhta hai  
🔴 But universal equality assume mat karo

---

# Related

- [[ROS 2 Node Mental Model]]
- [[Why Nodes Exist]]
- [[Node Runtime Flow]]
