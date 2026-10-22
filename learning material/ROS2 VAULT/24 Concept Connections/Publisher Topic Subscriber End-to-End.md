---
type: connection-map
status: locked
language: Hinglish
---

# Publisher → Topic → Subscriber End-to-End

Ye Batch 02 ka master mental model hai.

---

# Runtime

```text
Publisher Node Object
        │
        ├── Publisher Object
        │
        └── Timer Object
                 ↓
            Timer ready
                 ↓
          publisher callback
                 ↓
        String Message Object
                 ↓
          message.data fill
                 ↓
        publisher.publish(message)
                 ↓
             Topic
          /hello_topic
                 ↓
        ROS communication
                 ↓
       Subscription Object
                 ↓
       subscriber callback(msg)
                 ↓
          msg.data read
                 ↓
        "Hello from ROS2"
```

---

# Object Map

```text
Publisher Node
└── self.publisher_
      └── Publisher Object

Publisher callback
└── message
      └── String Message Object
           └── data

Subscriber Node
└── self.subscription
      └── Subscription Object

Subscriber callback
└── msg
      └── Received String Message Object
           └── data
```

---

# Registration vs Runtime

## Setup time

```python
create_publisher(...)
create_timer(..., callback_reference)
create_subscription(..., callback_reference, ...)
```

Resources + callbacks register/configure.

## Runtime

```text
spin
 ↓
event ready
 ↓
callback invocation
```

---

# Topic matching model

```text
Topic Name
+
Message Type
+
QoS Compatibility
```

---

# CLI around same graph

```text
ros2 topic list
→ channel exists?

ros2 topic type
→ message type?

ros2 topic info
→ endpoints?

ros2 topic echo
→ data?

ros2 topic hz
→ rate?

--verbose
→ QoS/endpoints?
```

---

# Actual proof

```text
/hello_topic
std_msgs/msg/String
1 Publisher
1 Subscriber
Hello from ROS2
~1 Hz
```

See [[LAB 03 — Topic CLI Inspection]].
