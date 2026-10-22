---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Package and Executable

## Package kya hai?

ROS 2 me package code organization ka fundamental unit hai.

Hamare learning project me important packages:

```text
my_first_pkg
my_first_interfaces
```

Historical use:

```text
my_first_pkg
→ Python nodes

my_first_interfaces
→ custom ROS interfaces
```

---

# Python package structure ka basic mental model

```text
my_first_pkg/
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
└── my_first_pkg/
    ├── __init__.py
    ├── simple_node.py
    ├── publisher_node.py
    └── ...
```

Top-level folder = ROS package.

Inner `my_first_pkg/` = Python module/package.

---

# Executable kya hai?

Example command:

```bash
ros2 run my_first_pkg simple_node
```

Breakdown:

```text
ros2 run
   ↓
package = my_first_pkg
   ↓
executable = simple_node
```

Python ROS packages me `setup.py` ke `console_scripts` section me mapping define hoti hai.

Example:

```python
' simple_node = my_first_pkg.simple_node:main'
```

Conceptually:

```text
simple_node
     ↓
my_first_pkg.simple_node
     ↓
main()
```

---

# Technical Refinement

Historical learning me isko simplified form me aise bola gaya tha:

> "`ros2 run` setup.py ko dekhta hai aur main() call karta hai."

More precise installed-package model:

```text
setup.py / package metadata
      ↓ build/install ke waqt
console script executable wrapper create/register hota hai
      ↓
ros2 run installed executable locate karta hai
      ↓
wrapper Python module import karta hai
      ↓
main() call hota hai
```

Meaning same learning goal ka hai:

> Executable name ko Python module ke `main()` se mapping milti hai.

---

# Package vs Executable vs Node

Ye teen same nahi hain.

```text
Package
│
├── Executable A
│      ↓
│    Node create kar sakta hai
│
├── Executable B
│      ↓
│    Node create kar sakta hai
│
└── Other files
```

Aur ek executable/process theoretically multiple nodes bhi create kar sakta hai.

See [[Node is not necessarily a Process]].

---

# Related

- [[main Function]]
- [[__name__ and __main__]]
- [[Node Runtime Flow]]
