---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 02 — Publisher Subscriber Hello

## Goal

Actual Publisher aur Subscriber nodes run karke verify karna ki message `/hello_topic` ke through flow ho raha hai.

---

# Build

Workspace:

```bash
cd ~/ros2_jazzy
colcon build
source ~/ros2_jazzy/install/setup.zsh
```

Shell zsh tha, isliye `.zsh` environment use hua.

---

# Initial mistake

Wrong package name use hua:

```bash
ros2 run my_first_package publisher_node
```

Result:

```text
Package 'my_first_package' not found
```

Actual package:

```text
my_first_pkg
```

See [[Package not found — my_first_package vs my_first_pkg]].

---

# Terminal 1 — Publisher

```bash
ros2 run my_first_pkg publisher_node
```

Actual log:

```text
[publisher_node]: Hello from ROS2
[publisher_node]: Hello from ROS2
...
```

---

# Terminal 2 — Subscriber

```bash
ros2 run my_first_pkg subscriber_node
```

Actual subscriber log:

```text
[subscriber_node]: Hello from ROS2
[subscriber_node]: Hello from ROS2
...
```

---

# What this proved

```text
Publisher Node
 ↓
String Message
 ↓
/hello_topic
 ↓
Subscriber Node
 ↓
callback(msg)
 ↓
msg.data
```

Theory me `/chatter` use hua tha, lekin actual package code me:

```text
/hello_topic
```

tha.

---

# Actual Publisher code core

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

Callback:

```python
message = String()
message.data = 'Hello from ROS2'
self.publisher_.publish(message)
```

---

# Learning

- Package name exact hona chahiye.
- Build + source practical workflow ka part hai.
- Publisher logs alone communication proof ka complete evidence nahi.
- Subscriber output ne end-to-end delivery verify ki.

Next: [[LAB 03 — Topic CLI Inspection]].
