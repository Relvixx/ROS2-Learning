---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 11 — Dynamic Reconfiguration

Timer callback every 2 sec current parameters read karta tha.

Initial output:

```text
Robot mode: normal | Max speed: 2.0
```

Repeated while node running.

---

# Runtime speed change

CLI se:

```text
max_speed → 4.0
```

Without node restart, next logs:

```text
Robot mode: normal | Max speed: 4.0
```

---

# Runtime mode change

Then:

```text
robot_mode → sport
```

Next logs:

```text
Robot mode: sport | Max speed: 4.0
```

---

# Practical conclusion

```text
Node stayed alive
 ↓
parameter set
 ↓
validation accepted
 ↓
stored value changed
 ↓
timer callback read current value
 ↓
runtime output/behavior changed
```

This was actual dynamic reconfiguration.
