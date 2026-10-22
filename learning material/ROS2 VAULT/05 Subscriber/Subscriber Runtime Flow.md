---
type: runtime-flow
status: locked
depth: must-know
language: Hinglish
---

# Subscriber Runtime Flow

```text
Program Start
 ↓
main()
 ↓
rclpy.init()
 ↓
Subscriber Node Object
 ↓
create_subscription()
 ↓
Subscription Object
 ↓
callback reference registered
 ↓
rclpy.spin(node)
 ↓
matching message arrives
 ↓
callback(msg)
 ↓
msg.data
 ↓
process / log
```

---

# Important

Subscriber continuously Python loop me Topic ko manually search nahi karta.

Event-driven mental model use karo:

```text
Wait
 ↓
Message Event
 ↓
Callback
 ↓
Wait
```

---

# Actual practical

Actual topic:

```text
/hello_topic
```

Actual subscriber logs:

```text
Hello from ROS2
Hello from ROS2
...
```

Publisher roughly 1 Hz par publish kar raha tha.

---

# Related

- [[rclpy spin]]
- [[Subscriber Callback]]
- [[LAB 02 — Publisher Subscriber Hello]]
