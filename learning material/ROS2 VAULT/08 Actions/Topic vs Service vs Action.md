---
type: comparison
status: locked
language: Hinglish
---

# Topic vs Service vs Action

| Pattern | Topic | Service | Action |
|---|---|---|---|
| Main idea | Publish/Subscribe | Request/Response | Goal/Feedback/Result |
| Sender side | Publisher | Client | Action Client |
| Receiver/worker side | Subscriber | Server | Action Server |
| Intermediate progress | not inherent | not inherent | Feedback |
| Final result concept | not inherent | Response | Result |
| Async object studied | callback/events | Future | two Futures + callbacks |

---

# Mental Models

## Topic

```text
Publisher
 ↓
Message
 ↓
Topic
 ↓
Subscriber
```

## Service

```text
Client
 ↓ Request
Server
 ↓ Response
Client
```

## Action

```text
Client
 ↓ Goal
Server
 ↓ Feedback
Client
 ↓
...progress...
 ↓
Server
 ↓ Final Result
Client
```

---

# Important

Ye comparison roles ko connect karta hai.

Mechanisms literally identical nahi.
