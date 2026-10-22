---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `create_service()`

Core:

```python
self.service = self.create_service(
    AddTwoInts,
    'add_two_ints',
    self.callback
)
```

---

# Kya hai?

✅ `Node` ka method.

❌ Class nahi.

Same pattern:

```text
create_publisher()
→ Publisher Object

create_subscription()
→ Subscription Object

create_service()
→ Service Object/handle
```

---

# Arguments

## `AddTwoInts`

Service Type / Interface.

## `'add_two_ints'`

Service Name.

Graph me:

```text
/add_two_ints
```

## `self.callback`

Callback **reference**.

Request aane par ROS us callback ko call karega.

---

# Callback Reference

```python
self.callback
```

not:

```python
self.callback()
```

See [[Callback Reference vs Invocation]].

---

# Related

- [[Service Server]]
- [[Server Service Callback]]
- [[Service Name vs Node Name]]
