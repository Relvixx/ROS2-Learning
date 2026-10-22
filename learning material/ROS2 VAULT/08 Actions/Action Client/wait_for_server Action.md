---
type: concept
status: locked
depth: medium
language: Hinglish
---

# Action `wait_for_server()`

Before Goal send:

```python
self._action_client.wait_for_server()
```

Mental model:

```text
Client
 ↓
"/fibonacci Action Server available?"
 ↓
wait until available
 ↓
Goal send flow continue
```

---

# Scope

Isko high-level server availability wait/check ke form me study kiya gaya.

Discovery internals deep nahi padhe gaye.
