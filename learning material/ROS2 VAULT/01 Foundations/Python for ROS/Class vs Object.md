---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Class vs Object

Node samajhne se pehle ye ROS-focused OOP revision kiya gaya tha.

---

# Class

Simple mental model:

> Class = Blueprint / Naksha

Example:

```python
class Robot:
    def move(self):
        print("Moving...")
```

Yahan abhi koi actual robot object create nahi hua.

Sirf structure/behavior define hua.

---

# Object

```python
robot1 = Robot()
```

Ab `Robot` class se ek object/instance bana.

```text
Robot
 ↓
Class / Blueprint

Robot()
 ↓
Object creation

robot1
 ↓
Object reference
```

---

# ROS connection

```python
class SimpleNode(Node):
    ...
```

Yahan `SimpleNode` ek class hai.

Abhi actual Node object create nahi hua.

Later:

```python
node = SimpleNode()
```

Ab `SimpleNode` ka actual object create hua.

---

# Important correction

Object ko sirf "blueprint access karne wali cheez" kehna incomplete hai.

Better:

> Object = class ka actual instance, jiske paas apna state/data hota hai aur class ke defined behavior/methods use kar sakta hai.

---

# ROS Mental Model

```text
Node class
   ↓ inherit
SimpleNode class
   ↓ instantiate
SimpleNode()
   ↓
actual node object
```

---

# Related

- [[self]]
- [[Inheritance and super]]
- [[ROS 2 Node Mental Model]]
