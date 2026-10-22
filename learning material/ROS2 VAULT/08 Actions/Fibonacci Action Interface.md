---
type: example
status: verified
depth: must-know
language: Hinglish
---

# Fibonacci Action Interface

Historical interface created:

```text
my_first_interfaces/action/Fibonacci
```

Source definition:

```text
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

---

# Goal Section

```text
int32 order
```

Meaning:

```text
Goal
└── order
```

Example:

```text
order = 6
```

---

# Result Section

```text
int32[] sequence
```

Meaning:

```text
Result
└── sequence
```

Example:

```text
[0, 1, 1, 2, 3, 5]
```

---

# Feedback Section

```text
int32[] partial_sequence
```

Meaning:

```text
Feedback
└── partial_sequence
```

Example progress:

```text
[0, 1]
[0, 1, 1]
[0, 1, 1, 2]
```

---

# Interface Verification Command

Historical implementation flow included:

```bash
ros2 interface show my_first_interfaces/action/Fibonacci
```

Expected/defined structure:

```text
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

---

# Source Consistency Note

Later debugging explanation guessed `partial_sequence` might be `int64[]`, but earlier explicit interface creation clearly used `int32[]`.

Vault canonical definition therefore stays:

```text
int32 / int32[]
```

Overflow lesson remains valid: ROS fixed-width integer fields have finite limits.

See [[Action Fixed Width Integer Overflow]].
