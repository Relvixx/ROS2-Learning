---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Runtime Parameter Change

Actual practical:

Initially:

```text
max_speed = 2.0
```

CLI:

```bash
ros2 param set /parameter_node max_speed 0.8
```

Output:

```text
Set parameter successful
```

Then:

```bash
ros2 param get /parameter_node max_speed
```

Output:

```text
Double value is: 0.8
```

---

# Runtime Flow

```text
Running Node
 ↓
max_speed = 2.0
 ↓
CLI set request
 ↓
max_speed = 0.8
 ↓
CLI get verifies
 ↓
0.8
```

---

# What this proved

Parameter value running node ke lifetime me change ho sakti hai.

Node source code default:

```text
2.0
```

phir bhi source file me same raha.

---

# Important boundary

At basic Parameters chapter:

```text
change accepted
```

observe kiya.

Next chapter asks:

```text
"What if requested value unsafe/invalid ho?"
```

See [[Callbacks and Validation — Boundary Note]].
