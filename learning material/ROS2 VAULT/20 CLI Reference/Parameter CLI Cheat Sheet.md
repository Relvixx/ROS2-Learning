---
type: cheat-sheet
status: practiced
language: Hinglish
---

# ⌨️ Parameter CLI Cheat Sheet

```bash
ros2 param list
```
→ available Node parameters

```bash
ros2 param get /parameter_node max_speed
```
→ current value

Actual initial:

```text
Double value is: 2.0
```

```bash
ros2 param set /parameter_node max_speed 0.8
```
→ runtime change

Actual:

```text
Set parameter successful
```

```bash
ros2 param get /parameter_node max_speed
```

Actual after set:

```text
Double value is: 0.8
```

```bash
ros2 param get /parameter_node use_sim_time
```

Observed:

```text
Boolean value is: False
```

```bash
ros2 param dump /parameter_node
```
→ parameter configuration dump/export

---

# Memory Flow

```text
LIST → GET → SET → GET AGAIN → DUMP
```

`GET AGAIN` important hai because change ko verify karna chahiye.
