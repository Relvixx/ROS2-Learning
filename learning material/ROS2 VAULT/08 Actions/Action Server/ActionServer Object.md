---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# ActionServer Object

Typical server setup:

```python
self._action_server = ActionServer(
    self,
    Fibonacci,
    'fibonacci',
    self.execute_callback
)
```

---

# Arguments

## `self`

Current Node object.

## `Fibonacci`

Action Interface / type.

## `'fibonacci'`

Action name.

Graph/CLI form:

```text
/fibonacci
```

## `self.execute_callback`

Callback method reference.

Not:

```python
self.execute_callback()
```

---

# Object relation

```text
FibonacciActionServer Node
└── _action_server
      ↓
   ActionServer Object
```

---

# Runtime

```text
ActionServer configured
 ↓
Goal arrives
 ↓
accepted/executed
 ↓
execute_callback(server_goal_handle)
```

---

# Related
- [[Action Server execute_callback]]
- [[Server Goal Handle]]
- [[Callback Reference vs Invocation]]
