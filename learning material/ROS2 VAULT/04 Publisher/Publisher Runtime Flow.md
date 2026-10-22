---
type: runtime-flow
status: locked
depth: must-know
language: Hinglish
---

# Publisher Runtime Flow

Publisher ko code lines ke collection ki jagah runtime story ki tarah padho.

---

# Conceptual learning example

```text
Program Start
 ↓
main()
 ↓
rclpy.init()
 ↓
Publisher Node Object
     │
     ├── create_publisher()
     │      ↓
     │   Publisher Object
     │
     └── create_timer()
            ↓
         Timer Object
 ↓
rclpy.spin(node)
 ↓
Timer event ready
 ↓
publish_message()
 ↓
msg = String()
 ↓
msg.data = "Hello"
 ↓
self.publisher_.publish(msg)
 ↓
configured Topic
```

---

# Four core building blocks

## 1. Publisher Object

```python
self.publisher_ = self.create_publisher(...)
```

→ Topic par correct message type publish karne wala resource.

## 2. Timer

```python
self.create_timer(...)
```

→ time-based callback trigger.

## 3. Message Object

```python
msg = String()
msg.data = "Hello"
```

→ actual payload structure.

## 4. Publish

```python
self.publisher_.publish(msg)
```

→ prepared Message Object Topic par send.

---

# Actual practical version

Later practical code:

```python
self.publisher_ = self.create_publisher(
    String,
    'hello_topic',
    10
)

self.timer = self.create_timer(
    1.0,
    self.timer_callback
)
```

callback:

```python
message = String()
message.data = 'Hello from ROS2'
self.publisher_.publish(message)
```

Actual observed rate:

```text
~1 Hz
```

See [[LAB 02 — Publisher Subscriber Hello]] and [[LAB 03 — Topic CLI Inspection]].

---

# Related

- [[Publisher Object and create_publisher]]
- [[Timer and Publisher Callback]]
- [[ROS Message Class vs Message Object]]
- [[Publisher Topic Subscriber End-to-End]]
