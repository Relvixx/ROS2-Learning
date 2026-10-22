---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Parameter Events

Command:

```bash
ros2 topic echo /parameter_events
```

Successful parameter changes can be observed via `/parameter_events`.

---

# Actual Event

After valid:

```text
max_speed → 4.0
```

observed:

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

# Decode

```text
node
→ kis node me change hua

new_parameters
→ new parameters

changed_parameters
→ existing parameters changed

deleted_parameters
→ removed parameters
```

---

# Important

Callback and event different roles:

```text
Callback
→ "change allow karna hai?"

Parameter Event
→ "actual change hua hai"
```

See [[Accepted vs Rejected Parameter Event]].
