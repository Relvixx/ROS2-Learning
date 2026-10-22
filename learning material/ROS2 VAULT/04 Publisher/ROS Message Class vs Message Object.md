---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# ROS Message Class vs Message Object

Publisher chapter me ye distinction important tha.

---

# Import

```python
from std_msgs.msg import String
```

Yahan:

```text
std_msgs
→ package

msg
→ message namespace

String
→ ROS message class/type
```

---

# Message Object

```python
msg = String()
```

Ab `String` class/type se ek Message Object bana.

Mental model:

```text
String
 ↓
Message Class / Type

String()
 ↓
Message Object create

msg
 ↓
Message Object reference
```

---

# Field

`String` message me important field:

```python
data
```

So:

```python
msg.data = "Hello"
```

means:

```text
msg
 ↓
String Message Object
 ↓
data field
 ↓
"Hello"
```

---

# Python string vs ROS String Message Object

Ye same nahi:

```python
"Hello"
```

→ normal Python `str`

```python
String()
```

→ ROS Message Object

ROS publisher expects correct ROS message type object.

---

# Publisher side

Publisher message create karta hua nahi maana gaya.

Code/callback create karta hai:

```python
msg = String()
msg.data = "Hello"
```

Publisher object:

```python
self.publisher_.publish(msg)
```

us prepared Message Object ko send karta hai.

---

# Subscriber side connection

Publisher:

```text
Message Object create
→ data write
```

Subscriber:

```text
Message Object receive
→ data read
```

See [[Received Message Object]].

---

# Related

- [[Publisher Runtime Flow]]
- [[Received Message Object]]
- [[Topic Name Message Type and QoS]]
