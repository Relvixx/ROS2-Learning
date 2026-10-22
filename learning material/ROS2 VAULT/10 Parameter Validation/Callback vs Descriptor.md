---
type: comparison
status: locked
depth: must-know
language: Hinglish
---

# Callback vs Descriptor

Ye final verification ka initially weak point tha, phir repair hua.

Final correct understanding:

> **Descriptor mostly static/general declared constraints deta hai. Callback custom/context-dependent runtime logic bhi laga sakta hai.**

---

# Descriptor

Example:

```text
acceleration must be 0.0 → 2.0
```

General range.

---

# Callback

Can express custom rules:

```text
if robot_mode == safe:
    max_speed <= 1.5
```

Context-dependent.

---

# Example Reasoning

Suppose:

```text
Descriptor:
max_speed 0.0 → 5.0

Current robot_mode:
safe

Callback:
safe mode → max_speed <= 1.5

Requested:
3.0
```

Then:

```text
Descriptor PASS ✅
Callback FAIL ❌
Final REJECT
```

Rahul correctly answered this after repair.

---

# Actual practical isolation

```text
max_speed = 8.0
→ custom callback rejected

acceleration = 5.0
→ descriptor range rejected
```

That experimentally separated the two mechanisms.
