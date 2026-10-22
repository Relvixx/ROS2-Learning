---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Node Owns Parameters

Parameters graph me floating global variables nahi hote.

Learning mental model:

> Parameter ek specific Node ke saath associated hota hai.

Actual CLI:

```bash
ros2 param get /parameter_node max_speed
```

Breakdown:

```text
/parameter_node
→ kis Node ka parameter?

max_speed
→ kaunsa parameter?
```

---

# Object relationship

```text
ParameterNode Object
└── ROS parameters
      └── max_speed
```

---

# Why CLI me Node name chahiye?

Because:

```text
same parameter name
```

different nodes ke andar possible ho sakta hai.

So identifying path:

```text
Node Name
+
Parameter Name
```

---

# Related

- [[Parameter Name Value Type]]
- [[Parameter CLI]]
