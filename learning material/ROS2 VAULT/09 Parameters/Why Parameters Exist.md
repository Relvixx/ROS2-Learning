---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Why Parameters Exist

Robot software me kaafi values aisi hoti hain jo **configuration** hain, core algorithm nahi.

Examples:

```text
max_speed
robot_mode
threshold
sensor_range
controller_gain
```

Agar har configuration change ke liye code edit karna pade:

```python
max_speed = 2.0
```

then:

```text
requirement changes
 ↓
source code edit
 ↓
rebuild / restart workflow
```

Ye flexible nahi.

---

# Parameter approach

```text
Node
└── Parameter
      ├── name
      ├── value
      └── type
```

Example:

```text
parameter_node
└── max_speed
      ├── value = 2.0
      └── type = double
```

---

# Simple definition

> **Parameter ek Node-associated named configuration value hai jise ROS 2 parameter system ke through inspect/configure kiya ja sakta hai.**

---

# Why useful?

Same node code ko different configuration ke saath use kar sakte ho.

```text
Same code
├── testing → lower speed
├── lab     → medium speed
└── robot   → different configured speed
```

---

# Important

Parameter:

❌ Topic nahi  
❌ normal Python variable ka synonym nahi  
❌ automatically robot behavior change karne wala magic object nahi

See:

- [[Parameter is not a Python Variable]]
- [[Parameter Change vs Behavior Change]]
