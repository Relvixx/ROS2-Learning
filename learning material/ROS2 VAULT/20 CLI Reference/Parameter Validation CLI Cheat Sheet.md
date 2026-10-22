---
type: cheat-sheet
status: verified
language: Hinglish
---

# ⌨️ Parameter Validation CLI Cheat Sheet

## List

```bash
ros2 param list /parameter_validation_node
```

Important observed:

```text
max_speed
robot_mode
start_type_description_service
use_sim_time
```

Later:

```text
acceleration
```

added.

---

## Callback Valid

```bash
ros2 param set /parameter_validation_node max_speed 3.5
```

```text
Set parameter successful
```

---

## Callback Invalid

```bash
ros2 param set /parameter_validation_node max_speed 8.0
```

```text
Setting parameter failed: max_speed must be between 0.0 and 5.0
```

---

## Allowed-value test

```bash
ros2 param set /parameter_validation_node robot_mode safe
```

success.

```bash
ros2 param set /parameter_validation_node robot_mode turbo
```

```text
Setting parameter failed: robot_mode must be safe, normal, or sport
```

---

## Descriptor test

```bash
ros2 param set /parameter_validation_node acceleration 1.5
```

success.

```bash
ros2 param set /parameter_validation_node acceleration 5.0
```

```text
Setting parameter failed: Parameter acceleration out of range Min: 0.0, Max: 2.0, value: 5.0
```

---

## Parameter Events

```bash
ros2 topic echo /parameter_events
```

Valid change generated event.

Rejected change generated no changed-parameter event.
