---
type: concept
status: introduced
depth: medium
language: Hinglish
---

# `wait_for_service()`

Client request bhejne se pehle Service available honi chahiye.

Common mechanism studied:

```python
self.client.wait_for_service(timeout_sec=1.0)
```

---

# Mental Model

```text
Client
 ↓
"Service available hai?"
 ↓
No → wait / retry
 ↓
Yes
 ↓
Request bhejo
```

---

# Important Scope

Is concept ko high-level availability check ke roop me padha gaya tha.

Deep discovery internals nahi padhe gaye.

---

# Related

- [[Service Client]]
- [[call_async]]
