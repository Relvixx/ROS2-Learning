---
type: runtime
status: locked
depth: must-know
language: Hinglish
---

# Accepted vs Rejected Parameter Event

## Accepted case

Request:

```text
max_speed = 4.0
```

Flow:

```text
request
 ↓
callback
 ↓
valid
 ↓
accepted
 ↓
stored value changes
 ↓
/parameter_events change event ✅
```

Actual event showed:

```text
changed_parameters:
- name: max_speed
  double_value: 4.0
```

---

# Rejected case

Request:

```text
max_speed = 9.0
```

Flow:

```text
request
 ↓
callback
 ↓
invalid
 ↓
successful=False
 ↓
stored value does not change
 ↓
no changed-parameter event
```

Actual observation:

> `/parameter_events` terminal me rejected `9.0` attempt ke liye kuch output nahi aaya.

This was live practical evidence.
