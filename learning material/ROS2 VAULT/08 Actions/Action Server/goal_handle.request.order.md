---
type: object-chain
status: locked
depth: must-know
language: Hinglish
---

# `goal_handle.request.order`

Nested object expression ko todho:

```python
goal_handle.request.order
```

---

# Tree

```text
goal_handle
└── request
    └── order
```

---

# Meaning

## `goal_handle`

Server Goal Handle.

## `.request`

Us goal se related request/goal data object.

## `.order`

Fibonacci Goal Interface ka field.

---

# Example

Client:

```python
goal_msg.order = 6
```

Server:

```python
order = goal_handle.request.order
```

Result:

```text
order = 6
```

---

# Why this note matters?

Ye Rahul ke learning pattern ka important object-chain example tha:

```text
object
└── attribute
    └── nested object
        └── field/value
```

---

# Related
- [[Server Goal Handle]]
- [[Goal Object]]
