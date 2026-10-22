---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Inheritance and `super()`

ROS Python nodes me common pattern:

```python
class SimpleNode(Node):
```

---

# Inheritance

Is line ko English/Hinglish me padho:

> Main `SimpleNode` naam ki class bana raha hu jo ROS ki `Node` class se inherit karti hai.

Mental model:

```text
Node
 ↓ provides ROS node capabilities
SimpleNode
 ↓ adds our custom behavior
```

---

# Why inheritance?

Hum ROS Node ki existing functionality reuse karte hain.

Examples:

- node name
- logging
- publisher creation
- subscription creation
- timer creation
- services/actions
- parameters
- clock

Sab zero se implement nahi karna padta.

---

# `super()`

Typical:

```python
super().__init__("simple_node")
```

High-level meaning:

> Parent `Node` class ka initialization run karo.

Isse base Node side properly initialize hoti hai.

---

# Learning boundary

`super()` ka Python internals-level implementation abhi required nahi tha.

Useful mental model:

```text
SimpleNode object creation
      ↓
SimpleNode.__init__()
      ↓
super().__init__("simple_node")
      ↓
Node base setup
      ↓
our custom initialization
```

---

# Related

- [[Class vs Object]]
- [[self]]
- [[ROS 2 Node Mental Model]]
- [[First Node Anatomy]]
