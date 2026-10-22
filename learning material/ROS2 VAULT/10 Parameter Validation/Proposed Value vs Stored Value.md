---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Proposed Value vs Stored Value

Suppose current:

```text
max_speed = 3.5
```

Request:

```text
max_speed = 8.0
```

Callback sees:

```text
proposed value = 8.0
```

It does **not** mean stored value already became 8.0.

---

# If rejected

```text
current stored = 3.5
requested      = 8.0
        ↓
callback
        ↓
successful=False
        ↓
request rejected
        ↓
stored remains 3.5
```

This exact behavior was practically verified.

See [[LAB 08 — Callback Validation]].
