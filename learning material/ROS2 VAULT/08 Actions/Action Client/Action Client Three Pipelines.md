---
type: mental-model
status: locked
depth: must-know
language: Hinglish
---

# Action Client — Three Pipelines

Action Client ko ek giant code block ki tarah mat yaad karo.

3 pipelines me yaad karo.

---

# 🟢 Pipeline 1 — Goal

```text
Goal Object
   ↓
send_goal_async()
   ↓
send_goal_future
   ↓
goal_response_callback()
   ↓
Client Goal Handle
   ↓
accepted?
```

---

# 🟡 Pipeline 2 — Feedback

```text
Server
   ↓
Feedback
   ↓
registered feedback_callback()
   ↓
feedback_msg.feedback
   ↓
partial_sequence
```

---

# 🔵 Pipeline 3 — Result

```text
Client Goal Handle
   ↓
get_result_async()
   ↓
get_result_future
   ↓
get_result_callback()
   ↓
future.result().result
   ↓
Action Result Object
   ↓
result.sequence
```

---

# Underneath everything

```text
rclpy.spin(action_client)
```

ROS events/callback processing ko active rakhta hai.

---

# Related
- [[Action Runtime Flow]]
- [[rclpy spin]]
