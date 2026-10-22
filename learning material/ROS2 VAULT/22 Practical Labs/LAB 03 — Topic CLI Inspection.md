---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 03 — Topic CLI Inspection

Publisher aur Subscriber run karne ke baad ROS graph ko CLI se inspect kiya.

---

# Step 1 — Topic list

```bash
ros2 topic list
```

Actual output:

```text
/hello_topic
/parameter_events
/rosout
```

Important discovery:

> Theory ka `/chatter` actual code me `/hello_topic` tha.

---

# Step 2 — Message type

```bash
ros2 topic type /hello_topic
```

Actual:

```text
std_msgs/msg/String
```

---

# Step 3 — Endpoint info

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
1 Publisher
+
1 Subscriber
```

graph par matched.

---

# Step 4 — Live data

```bash
ros2 topic echo /hello_topic
```

Actual:

```text
data: Hello from ROS2
---
data: Hello from ROS2
---
```

Important observation:

> `echo` itself Topic data receive karta hai, so running echo additional subscription create kar sakta hai.

---

# Step 5 — Rate

```bash
ros2 topic hz /hello_topic
```

Actual:

```text
average rate: 1.000
min: ~0.999s
max: ~1.000s
```

Conclusion:

```text
≈ 1 message / second
≈ 1 Hz
```

Ye Publisher timer ke 1.0 second period se align hua.

---

# Step 6 — QoS inspection

```bash
ros2 topic info /hello_topic --verbose
```

Observed Publisher:

```text
Reliability: RELIABLE
Durability: VOLATILE
```

Observed Subscriber:

```text
Reliability: RELIABLE
Durability: VOLATILE
```

CLI ne History (Depth) `UNKNOWN` report kiya tha.

---

# Full evidence chain

```text
TOPIC EXISTS
/hello_topic
      ↓
TYPE
std_msgs/msg/String
      ↓
CONNECTION
1 Publisher + 1 Subscriber
      ↓
DATA
Hello from ROS2
      ↓
RATE
~1 Hz
      ↓
QoS
RELIABLE + VOLATILE observed
```

Ye chapter ka strongest practical verification tha.

---

# Related

- [[Topic CLI]]
- [[Topic Debugging Flow]]
- [[QoS Fundamentals]]
