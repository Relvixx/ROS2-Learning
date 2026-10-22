---
type: concept
status: verified-later
depth: must-know
language: Hinglish
---

# Parameter Change vs Behavior Change

Ye distinction basic Parameters ke baad callbacks/dynamic reconfiguration discussion me explicitly lock hua.

---

# Parameter stored value changes

```text
max_speed
2.0 → 0.8
```

✅ Parameter state changed.

But suppose control code:

```python
motor_speed = 2.0
```

hardcoded hi use kar raha hai.

Then:

```text
Parameter = 0.8
but
Behavior still uses 2.0
```

---

# Result

> **Parameter value change hona aur Node behavior change hona automatically same cheez nahi hai.**

Node ko current parameter value ko behavior me consume/use karna padega.

---

# Example pattern

```python
speed = self.get_parameter('max_speed').value
```

Agar behavior repeatedly current parameter read karta hai:

```text
CLI set
 ↓
parameter changes
 ↓
next behavior calculation reads new value
 ↓
behavior changes
```

---

# Why included in Batch 05?

Ye basic Parameters ka essential engineering correction hai, even though dynamic-reconfiguration implementation next chapter me deepen hua.
