---
type: debugging-model
status: verified
depth: must-know
language: Hinglish
---

# Topic Debugging Flow

Random commands throw mat karo.

Systematically evidence collect karo.

---

# Recommended flow

```text
LIST
 ↓
Topic exist karta hai?
 ↓
TYPE
 ↓
Expected message type hai?
 ↓
INFO
 ↓
Publisher / Subscriber endpoints present?
 ↓
ECHO
 ↓
Actual data aa raha hai?
 ↓
HZ
 ↓
Rate expected hai?
 ↓
VERBOSE
 ↓
QoS / endpoint details inspect
```

---

# Commands

```bash
ros2 topic list
```

```bash
ros2 topic type /hello_topic
```

```bash
ros2 topic info /hello_topic
```

```bash
ros2 topic echo /hello_topic
```

```bash
ros2 topic hz /hello_topic
```

```bash
ros2 topic info /hello_topic --verbose
```

---

# Actual practical evidence

## Topic

```text
/hello_topic
```

## Type

```text
std_msgs/msg/String
```

## Connections

```text
Publisher count: 1
Subscription count: 1
```

## Data

```text
Hello from ROS2
```

## Rate

```text
~1 Hz
```

## QoS observed

```text
RELIABLE
VOLATILE
```

---

# Why this is engineering-style debugging?

Har step ek question answer karta hai.

```text
Symptom
 ↓
Evidence
 ↓
Hypothesis
 ↓
Test
 ↓
Root Cause
```

Topic debugging me bhi same philosophy.

---

# Related

- [[Topic CLI]]
- [[LAB 03 — Topic CLI Inspection]]
