---
type: concept
status: locked-basic
depth: medium
language: Hinglish
---

# QoS Fundamentals

QoS = **Quality of Service**

ROS 2 Publisher aur Subscriber communication behavior ko policies ke through configure karta hai.

Learning ke current basic level par policies ke naam:

```text
QoS
├── Reliability
├── Durability
├── History
└── Depth
```

---

# `10` ka correct mental model

Examples:

```python
create_publisher(String, "chatter", 10)
create_subscription(String, "chatter", callback, 10)
```

Learning ke beginning me `10` ko simple "queue size" analogy diya gaya tha.

Later refinement:

> Ye shorthand QoS history depth-style configuration se related hai.

Important:

```text
10
≠
"har situation me permanently exactly 10 messages store honge"
```

Actual behavior QoS policy context par depend karta hai.

---

# Exact same QoS required?

❌ Nahi.

Correct locked mental model:

> Publisher aur Subscriber ki QoS settings **compatible** honi chahiye. Exact identical hona zaroori nahi.

Example discussed:

```text
Publisher depth = 10
Subscriber depth = 5
```

Sirf depth different hone se automatically ye conclude nahi kar sakte:

```text
communication impossible
```

---

# Actual practical observation

`ros2 topic info /hello_topic --verbose`

me observed:

```text
Publisher:
Reliability: RELIABLE
Durability: VOLATILE

Subscriber:
Reliability: RELIABLE
Durability: VOLATILE
```

History depth CLI output me `UNKNOWN` report hua tha.

---

# Knowledge Boundary

## 🟢 Current level

- QoS ka purpose high-level
- Reliability / Durability / History / Depth names
- Depth intuition
- compatibility matters

## 🔴 Deep nahi padha

- full Request/Offered compatibility matrix
- sensor-data QoS profiles
- deadline/liveliness internals
- DDS QoS internals

---

# Related

- [[Topic Name Message Type and QoS]]
- [[Topic CLI]]
