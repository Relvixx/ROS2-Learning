---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# `main()` Function

## Sabse important point

`main` Python ka reserved keyword nahi hai.

Ye ek normal function hai.

```python
def main():
    print("Program Started")
```

Naam technically kuch aur bhi ho sakta tha:

```python
def rahul():
    ...
```

Lekin `main` ek common convention hai jo program ke primary entry function ko represent karta hai.

---

# Definition ≠ Execution

```python
def main():
    print("Hello")
```

Output:

```text
kuch nahi
```

Kyun?

Function define hua hai, call nahi hua.

See [[Function Definition vs Invocation]].

---

# ROS code me role

Typical ROS Python node:

```python
def main(args=None):
    rclpy.init(args=args)

    node = SimpleNode()

    rclpy.spin(node)

    rclpy.shutdown()
```

Story:

```text
main()
 ↓
ROS initialize
 ↓
Node object create
 ↓
event processing
 ↓
shutdown
```

---

# `ros2 run` se connection

Python ROS package me executable mapping `main()` tak point karti hai.

Example:

```python
simple_node = my_first_pkg.simple_node:main
```

Meaning:

```text
Executable name
      ↓
Python module
      ↓
main function
```

---

# `python3 file.py` se connection

Agar file direct Python se run hoti hai, common pattern:

```python
if __name__ == "__main__":
    main()
```

See [[__name__ and __main__]].

---

# Mental Model

```text
main()
=
program ke important startup steps ka organized entry function
```

Ye ROS-specific function nahi hai.

---

# Related

- [[Function Definition vs Invocation]]
- [[__name__ and __main__]]
- [[Node Runtime Flow]]
