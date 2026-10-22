---
type: correction
status: canonical
language: Hinglish
---

# Executable Name is not ROS Node Name

Actual:

```text
executable = parameter_node
node name  = config_node
```

Multi-node:

```text
publisher_node → /launch_publisher
subscriber_node → /launch_subscriber
```

Executable package installation/run target hai.

Node name ROS graph identity.
