---
type: structure
status: verified
language: Hinglish
---

# Launch Folder Structure

Python ROS package:

```text
my_first_pkg/
├── my_first_pkg/
│   ├── parameter_node.py
│   ├── publisher_node.py
│   └── subscriber_node.py
│
├── launch/
│   ├── parameter.launch.py
│   └── multi_nodes.launch.py
│
├── package.xml
├── setup.py
└── setup.cfg
```

---

# Important separation

```text
my_first_pkg/my_first_pkg/
→ Python node source code

my_first_pkg/launch/
→ Launch files
```

Naming convention learned:

```text
something.launch.py
```

Example:

```text
parameter.launch.py
multi_nodes.launch.py
```

But creating source file alone enough nahi.

It must be installed into package share space.

See [[Installing Launch Files with setup.py]].
