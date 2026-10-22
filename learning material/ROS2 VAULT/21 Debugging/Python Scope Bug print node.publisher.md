---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Python Scope Bug — `print(node.publisher_)`

Actual source:

```python
def main(args=None):
    rclpy.init(args=args)

    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


print(node.publisher_)
```

---

# Problem

```text
node
```

`main()` ke andar local variable tha.

Outside `main()`:

```python
print(node.publisher_)
```

Python global scope me `node` dhoond raha tha.

Not found → `NameError`.

---

# Mental Structure

```text
main()
└── node
    └── publisher_
```

Outside function:

```text
node unavailable
```

---

# Fix

Old debug line remove ki gayi:

```python
print(node.publisher_)
```

Then publisher launched successfully.

---

# Lesson

Ye:

```text
Launch bug
```

nahi tha.

Ye:

```text
plain Python scope bug
```

tha.

Traceback → exact source line → scope reasoning → fix.
