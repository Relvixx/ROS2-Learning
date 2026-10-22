---
type: python-reference
status: verified
language: Hinglish
---

# `glob()` for Launch Files

Import:

```python
from glob import glob
```

Use:

```python
glob('launch/*.launch.py')
```

Meaning:

> `launch/` folder me pattern match karne wali `.launch.py` files find karo.

---

# Example

Folder:

```text
launch/
├── parameter.launch.py
├── multi_nodes.launch.py
└── notes.txt
```

Pattern:

```python
glob('launch/*.launch.py')
```

conceptually matches:

```text
parameter.launch.py
multi_nodes.launch.py
```

not:

```text
notes.txt
```

---

# Why useful?

Nayi matching launch file add karne par same pattern usko include kar sakta hai.

Actual `multi_nodes.launch.py` ke liye separate setup.py entry add nahi karni padi.
