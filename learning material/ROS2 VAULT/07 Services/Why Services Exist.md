---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Why Services Exist

Topics ke baad next communication pattern tha:

> **Request → Response**

Topic me Publisher data publish karta hai aur Subscribers receive karte hain.

Service me ek Client specific request bhejta hai aur Server us request ke liye response deta hai.

---

# Mental Model

```text
Client
  │
  │ Request
  ▼
Server
  │
  │ Response
  ▼
Client
```

---

# Example — Add Two Integers

Client request:

```text
a = 5
b = 7
```

Server processing:

```text
5 + 7
```

Response:

```text
sum = 12
```

---

# Service ko "synchronous" kyun nahi bolna chahiye?

Communication pattern:

```text
Request / Response
```

hai.

Lekin client API asynchronous ho sakti hai.

Humne specifically:

```python
call_async()
```

use kiya.

So correct mental model:

> **Service = request/response communication pattern. Client handling synchronous ya asynchronous API style me ho sakti hai.**

---

# Topic se difference

```text
TOPIC
Publisher → Message → Subscriber

SERVICE
Client → Request → Server
Client ← Response ← Server
```

See [[Topic vs Service]].

---

# Related

- [[Service Interface]]
- [[Service Server]]
- [[Service Client]]
- [[Service Runtime Flow]]
