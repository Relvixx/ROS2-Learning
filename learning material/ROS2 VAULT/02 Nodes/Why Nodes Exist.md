---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Why Nodes Exist

## Problem

Robot ek single kaam nahi karta.

Example robot:

```text
Camera
LiDAR
Motor Control
GPS
Object Detection
Navigation
```

Agar poora robot ek giant monolithic program me ho:

```text
One Giant Program
├── Camera
├── LiDAR
├── Motor
├── GPS
├── AI
└── Navigation
```

to debugging, reuse, replacement aur system design difficult ho sakta hai.

---

# ROS approach

System ko computational units me divide karo.

```text
Robot System
├── Camera Node
├── LiDAR Node
├── Motor Node
├── GPS Node
└── Detection Node
```

Har Node ka generally focused responsibility hota hai.

---

# Important distinction

Node ka **primary purpose sirf communication karna nahi** hai.

Better mental model:

```text
Node
 ↓
specific computation / responsibility
 ↓
zarurat pade to
 ↓
ROS communication resources use karta hai
```

Examples:

### Camera Node

Primary responsibility:
→ camera data acquire/process karna

Communication:
→ image publish kar sakta hai

### Motor Controller Node

Primary responsibility:
→ motor control

Communication:
→ velocity command receive kar sakta hai

---

# Why modularity valuable hai?

- Ek component alag debug kar sakte ho.
- Ek component replace kar sakte ho.
- Same component dusre robot me reuse ho sakta hai.
- Different nodes alag languages/process arrangements me ho sakte hain.
- System graph clearer hota hai.

---

# Precise definition

> ROS 2 Node ek computational unit / ROS participant hai jo specific responsibility perform karta hai aur ROS graph me communication/resources create kar sakta hai.

See [[Node is not necessarily a Process]].

---

# Related

- [[ROS 2 Node Mental Model]]
- [[ROS 2 Ecosystem]]
