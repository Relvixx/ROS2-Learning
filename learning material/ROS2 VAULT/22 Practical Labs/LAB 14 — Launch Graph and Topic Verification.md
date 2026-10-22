---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 14 — Launch Graph and Topic Verification

Multi-node launch running tha.

---

# Node Graph

```bash
ros2 node list
```

Actual:

```text
/launch_publisher
/launch_subscriber
```

Proof:

```text
both launched ROS nodes exist ✅
```

---

# Topic Relationship

```bash
ros2 topic info /hello_topic
```

Actual:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

Proof:

```text
publisher endpoint ✅
subscriber endpoint ✅
```

---

# Live Data

```bash
ros2 topic echo /hello_topic
```

Actual repeated:

```text
data: Hello from ROS2
---
```

Proof:

```text
nodes started
+
ROS graph connected
+
actual message flow working
```

---

# End-to-End

```text
ros2 launch
 ↓
2 Node actions
 ↓
2 processes
 ↓
2 ROS graph nodes
 ↓
/hello_topic
 ↓
live String data
```

This is the strongest Launch Files practical verification.
