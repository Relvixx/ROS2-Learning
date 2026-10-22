---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Launch `package`, `executable`, `name`

Example:

```python
Node(
    package='my_first_pkg',
    executable='parameter_node',
    name='config_node'
)
```

---

# `package`

```text
my_first_pkg
```

Target executable kis ROS package me hai.

---

# `executable`

```text
parameter_node
```

Kaunsa installed runnable target start karna hai.

Connection:

```text
setup.py console_scripts
'parameter_node = my_first_pkg.parameter_node:main'
```

and launch:

```text
executable='parameter_node'
```

---

# `name`

```text
config_node
```

Running ROS graph identity/name.

---

# Mental Map

```text
package
→ kahan?

executable
→ kya run?

name
→ graph me kis naam se?
```

See [[Executable Name vs Node Name]].
