---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 10 — Parameter Events

Terminal 1:

```bash
ros2 topic echo /parameter_events
```

Terminal 2 valid change:

```bash
ros2 param set /parameter_validation_node max_speed 4.0
```

Actual event:

```text
node: /parameter_validation_node
new_parameters: []
changed_parameters:
- name: max_speed
  value:
    type: 3
    double_value: 4.0
deleted_parameters: []
```

---

# Invalid Experiment

Then:

```bash
ros2 param set /parameter_validation_node max_speed 9.0
```

Callback rejected it.

Actual observation from event terminal:

```text
kuch new output nahi aaya
```

---

# Final Proof

```text
Accepted request
→ stored value changes
→ event ✅

Rejected request
→ stored value unchanged
→ changed event ❌
```
