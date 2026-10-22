---
type: correction
status: canonical
language: Hinglish
---

# Wrong Parameter Name — `robot_node` vs `robot_mode`

Actual mistake:

```bash
ros2 param get /parameter_validation_node robot_node
```

Output:

```text
Parameter not set
```

Correct declared name:

```text
robot_mode
```

Lesson:

> Node name, parameter name aur values exact identifiers hain. Similar-looking names interchangeable nahi.
