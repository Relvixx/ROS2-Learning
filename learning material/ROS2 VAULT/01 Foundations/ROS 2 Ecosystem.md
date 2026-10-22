---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# ROS 2 Ecosystem

## Why ye note important hai?

Node directly hawa me exist nahi karta.

Humne learning restart karte waqt sabse pehle ye chain banayi thi:

```text
Ubuntu
   ↓
ROS 2 Installed
   ↓
Workspace
   ↓
Package
   ↓
Executable
   ↓
Node
```

Agar ye chain clear nahi hai to `ros2 run`, `setup.py`, package aur Node disconnected syntax lagte hain.

---

# 1. Ubuntu / Operating System

Ubuntu wo operating system hai jiske upar hamara ROS 2 environment chal raha tha.

Hamare learning environment me:

```text
OS: Ubuntu
ROS 2 Distribution: Jazzy Jalisco
Shell: zsh
Workspace: ~/ros2_jazzy
Language: Python / rclpy
```

Is note ka goal Ubuntu install procedure sikhana nahi hai.

> Attached learning history me detailed "Ubuntu install from zero" lesson preserved nahi mila, isliye wo knowledge yahan invent nahi ki gayi hai.

---

# 2. ROS 2 Environment

ROS 2 libraries, tools aur communication infrastructure provide karta hai.

Python side par important library:

```python
import rclpy
```

`rclpy` = ROS Client Library for Python.

Iske through Python code ROS 2 functionality use karta hai.

---

# 3. Workspace

Example:

```text
~/ros2_jazzy
```

Workspace ek directory hai jisme ROS 2 packages organize, build aur install hote hain.

See [[Workspace]].

---

# 4. Package

Example:

```text
my_first_pkg
```

Package related ROS software ko organize karta hai.

Ek package ke andar multiple nodes ho sakte hain.

See [[Package and Executable]].

---

# 5. Executable

`ros2 run` package ke andar se ek installed executable ko run karta hai.

Example:

```bash
ros2 run my_first_pkg simple_node
```

Yahan:

```text
my_first_pkg → package
simple_node  → executable name
```

Python packages me `console_scripts` executable mapping ka important part hai.

See [[Package and Executable]].

---

# 6. Node

Executable run hone ke baad code `main()` tak pahunchta hai, ROS initialize hota hai aur Node object create ho sakta hai.

Precise mental model:

> Node ek ROS 2 computational unit / participant hai.

See [[ROS 2 Node Mental Model]].

---

# Full Connection

```text
Operating System
     ↓
ROS 2 installed
     ↓
Workspace
     ↓
Package
     ↓
Installed executable
     ↓
main()
     ↓
rclpy.init()
     ↓
Node object
     ↓
spin / event processing
```

---

# Knowledge Boundary

## 🟢 Must know

- Workspace package ko contain karta hai.
- Package software organization unit hai.
- Executable `ros2 run` se start hota hai.
- Node ROS system ka computational participant hai.
- `rclpy` Python ko ROS 2 functionality deta hai.

## 🔴 Abhi nahi

- DDS implementation internals
- ament source code
- colcon internals
- Python packaging internals
