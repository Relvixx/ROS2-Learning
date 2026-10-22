---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# `__name__` and `__main__`

## Problem kya solve hoti hai?

Maan lo:

```python
def main():
    print("Calculator Started")

main()
```

Agar ye module kisi doosri Python file me import hua:

```python
import calculator
```

to top-level `main()` bhi execute ho jayega.

Kabhi-kabhi hume sirf functions/classes import karni hoti hain, program auto-start nahi karna hota.

---

# Direct run case

```bash
python3 calculator.py
```

Direct execution par Python:

```python
__name__ = "__main__"
```

set karta hai.

Isliye:

```python
if __name__ == "__main__":
    main()
```

condition true ho jati hai.

---

# Import case

```python
import calculator
```

Is case me module ka `__name__` us module ke naam jaisa hota hai:

```text
calculator
```

Isliye:

```python
if __name__ == "__main__":
```

false hota hai.

`main()` auto-run nahi hota.

---

# Simple definition

> `if __name__ == "__main__":` ensure karta hai ki direct file execution par `main()` chale, lekin normal import ke time auto-run na ho.

---

# ROS connection

ROS executable path:

```text
ros2 run ...
   ↓
installed console-script executable
   ↓
module import
   ↓
main() call
```

Is path me `if __name__ == "__main__":` block main trigger nahi hota.

Lekin same file ko direct run karne ki possibility ke liye block useful hota hai:

```bash
python3 simple_node.py
```

---

# Two Gates Mental Model

```text
                  main()
                 ▲     ▲
                /       \
console-script wrapper   direct python file
(ros2 run)               (__name__ == "__main__")
```

Destination same ho sakta hai:

```text
main()
```

Entry mechanism alag hai.

---

# Knowledge Boundary

## 🟢 Must know

- `__name__` Python module variable hai.
- Direct execution par `__name__ == "__main__"`.
- Import par normally module name hota hai.
- Guard unwanted auto-execution se bachata hai.
- `ros2 run` console-script entry se `main()` tak pahunchta hai.

## 🔴 Abhi nahi

- Python import machinery internals
- importlib internals
- Python interpreter source code

---

# Related

- [[main Function]]
- [[Package and Executable]]
