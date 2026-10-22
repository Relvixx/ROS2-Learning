---
type: correction
status: canonical
language: Hinglish
---

# QoS Depth is not Permanent 10-Message Storage

Early beginner intuition:

```text
10 = Queue Size
```

Useful analogy thi, lekin incomplete.

Refined learning:

```text
10
→ QoS history depth-style shorthand in these APIs
```

Important:

```text
10
≠
"ROS always permanently stores exactly 10 messages"
```

Actual behavior depends on QoS policy context.

Also:

```text
Publisher depth 10
Subscriber depth 5
```

sirf is difference ki wajah se automatically communication impossible conclude nahi karna.

Correct idea:

> QoS policies compatible honi chahiye.

See [[QoS Fundamentals]].
