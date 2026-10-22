---
type: cli-reference
status: verified
depth: must-know
language: Hinglish
---

# Topic CLI

ROS Topic ko terminal se inspect/debug karne ke important commands.

---

# 1. List — Names

```bash
ros2 topic list
```

Current graph ke topic names.

Actual practical me:

```text
/hello_topic
/parameter_events
/rosout
```

---

# 2. Type — Message Type

```bash
ros2 topic type /hello_topic
```

Actual:

```text
std_msgs/msg/String
```

---

# 3. Info — Connections

```bash
ros2 topic info /hello_topic
```

Actual practical:

```text
Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1
```

---

# 4. Echo — Actual Data

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

Important mental model:

> `ros2 topic echo` Topic data receive karne ke liye communication me participate karta hai; ye magic screen-reader nahi.

---

# 5. Hz — Rate

```bash
ros2 topic hz /hello_topic
```

Actual measured:

```text
average rate: 1.000
```

≈ 1 message / second.

---

# 6. Verbose Info — Endpoint + QoS Details

```bash
ros2 topic info /hello_topic --verbose
```

Useful for:

- publisher/subscriber endpoint
- node name
- reliability
- durability
- other QoS information

---

# 7. Manual Publish

Theory example:

```bash
ros2 topic pub --once \
/chatter \
std_msgs/msg/String \
"{data: 'Hello'}"
```

Meaning:

```text
--once
→ one publication

/chatter
→ Topic

std_msgs/msg/String
→ Message type

{data: 'Hello'}
→ message fields/value
```

Repeated rate example:

```bash
ros2 topic pub -r 5 \
/chatter \
std_msgs/msg/String \
"{data: 'Hello'}"
```

`-r 5` → approximately 5 Hz.

---

# 8. Interface Structure

```bash
ros2 interface show std_msgs/msg/String
```

Message interface ke fields/structure inspect karta hai.

---

# Additional commands discussed

```bash
ros2 topic find std_msgs/msg/String
```

→ given message type use karne wale Topics find karna.

```bash
ros2 topic bw /hello_topic
```

→ bandwidth observation.

```bash
ros2 topic delay /hello_topic
```

→ delay-related observation where supported/applicable.

Exact CLI subcommand support distribution/version ke hisaab se vary kar sakta hai.

---

# Memory Map

| Command | Yaad rakhne ka word |
|---|---|
| `list` | NAME |
| `type` | TYPE |
| `info` | CONNECTIONS |
| `echo` | DATA |
| `hz` | RATE |
| `pub` | MANUAL PUBLISH |
| `interface show` | STRUCTURE |
| `--verbose` | ENDPOINT/QoS DETAILS |

---

# Related

- [[Topic Debugging Flow]]
- [[LAB 03 — Topic CLI Inspection]]
