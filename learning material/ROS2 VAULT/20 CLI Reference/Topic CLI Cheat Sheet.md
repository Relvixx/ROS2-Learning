---
type: cheat-sheet
status: verified
language: Hinglish
---

# ⌨️ Topic CLI Cheat Sheet

```bash
ros2 topic list
```
→ Topic names

```bash
ros2 topic type /hello_topic
```
→ Message type

```bash
ros2 topic info /hello_topic
```
→ Type + publisher/subscriber counts

```bash
ros2 topic info /hello_topic --verbose
```
→ Endpoint + QoS details

```bash
ros2 topic echo /hello_topic
```
→ Live message data

```bash
ros2 topic hz /hello_topic
```
→ Message frequency

```bash
ros2 interface show std_msgs/msg/String
```
→ Message interface structure

```bash
ros2 topic pub --once /chatter std_msgs/msg/String "{data: 'Hello'}"
```
→ One manual publish

```bash
ros2 topic pub -r 5 /chatter std_msgs/msg/String "{data: 'Hello'}"
```
→ Repeated ~5 Hz publish

---

# Debug order

```text
list → type → info → echo → hz → verbose
```

See [[Topic Debugging Flow]].
