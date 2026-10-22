---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Why Parameter Validation Exists

Basic Parameters me humne seekha:

```text
DECLARE
 ↓
READ
 ↓
CLI SET
 ↓
VERIFY
```

Lekin robotics me ek problem hai.

Suppose:

```text
max_speed = 2.0
```

Koi runtime par request bhejta hai:

```bash
ros2 param set /parameter_validation_node max_speed -50.0
```

Ya:

```text
max_speed = 999999.0
```

Kya har requested value blindly accept honi chahiye?

**Nahi.**

---

# Core Problem

```text
Parameter Set Request
        ↓
    Is value safe?
        ↓
   ┌────┴────┐
   ↓         ↓
 VALID     INVALID
   ↓         ↓
ACCEPT     REJECT
```

Yahi [[Parameter Callback Mental Model]] solve karta hai.
