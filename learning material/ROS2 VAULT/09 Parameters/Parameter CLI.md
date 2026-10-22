---
type: cli-reference
status: practiced
depth: must-know
language: Hinglish
---

# Parameter CLI

---

# 1. List

```bash
ros2 param list
```

Actual observed:

```text
/parameter_node:
  max_speed
  start_type_description_service
  use_sim_time
```

This showed parameters associated with `/parameter_node`.

---

# 2. Get

```bash
ros2 param get /parameter_node max_speed
```

Actual initial output:

```text
Double value is: 2.0
```

---

# 3. Set

```bash
ros2 param set /parameter_node max_speed 0.8
```

Actual:

```text
Set parameter successful
```

---

# 4. Verify again

```bash
ros2 param get /parameter_node max_speed
```

Actual:

```text
Double value is: 0.8
```

---

# 5. `use_sim_time`

Actual:

```bash
ros2 param get /parameter_node use_sim_time
```

Output:

```text
Boolean value is: False
```

This parameter was observed but not deeply studied in the basic Parameters lesson.

---

# 6. Dump

Covered command:

```bash
ros2 param dump /parameter_node
```

Purpose at learned level:

> Node ke parameter values ko YAML-style configuration form me dump/export karna.

Exact terminal output from Rahul's original basic practical is not preserved in current sources, so this vault does not fabricate it.

---

# Command Mental Map

```text
list
→ kya parameters hain?

get
→ current value kya hai?

set
→ runtime value change karo

dump
→ parameter configuration export/dump
```
