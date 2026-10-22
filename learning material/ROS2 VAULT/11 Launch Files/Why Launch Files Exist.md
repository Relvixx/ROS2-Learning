---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Why Launch Files Exist

Ab tak individual node:

```bash
ros2 run my_first_pkg publisher_node
```

alag terminal me start kar sakte the.

Small project me okay.

Real robot imagine karo:

```text
Robot System
├── Camera Node
├── LiDAR Node
├── Motor Controller
├── Localization Node
├── Navigation Node
├── Safety Node
└── Diagnostics Node
```

Har node manually alag terminal me start karna scalable nahi.

---

# Launch System ka role

> **System ko components + configuration ke saath systematically start/orchestrate karna.**

Mental model:

```text
            Launch File
                │
        ┌───────┼───────┐
        ↓       ↓       ↓
      Node A  Node B   Node C
```

One command:

```bash
ros2 launch ...
```

---

# Sirf multiple nodes start karna?

Nahi.

Launch system broader configuration/orchestration layer hai.

Actual learned/basic scope me:

```text
which package
which executable
runtime node name
startup parameters
multiple node actions
```

Advanced namespaces/conditions/remapping/include were not actually learned in this chapter, so unko yahan mastery ke roop me claim nahi kiya gaya.
