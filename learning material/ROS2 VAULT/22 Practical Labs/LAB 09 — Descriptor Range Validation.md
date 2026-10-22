---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 09 — Descriptor Range Validation

Third parameter:

```text
acceleration = 1.0
```

Descriptor range:

```text
0.0 → 2.0
step = 0.1
```

Important:

> `parameter_callback()` me acceleration ka custom validation intentionally nahi tha.

---

# Initial

```bash
ros2 param get /parameter_validation_node acceleration
```

Actual:

```text
Double value is: 1.0
```

---

# Valid

```bash
ros2 param set /parameter_validation_node acceleration 1.5
```

Actual:

```text
Set parameter successful
```

Verify:

```text
Double value is: 1.5
```

---

# Invalid

```bash
ros2 param set /parameter_validation_node acceleration 5.0
```

Actual:

```text
Setting parameter failed: Parameter acceleration out of range Min: 0.0, Max: 2.0, value: 5.0
```

---

# Proof

```text
acceleration callback rule
→ none

descriptor constraint
→ 0.0–2.0

request 5.0
→ rejected
```

So descriptor constraint independently enforced hua.
