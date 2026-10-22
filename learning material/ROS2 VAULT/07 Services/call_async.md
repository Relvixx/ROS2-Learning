---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `call_async()`

Service Client chapter ka central method.

```python
future = self.client.call_async(request)
```

---

# Breakdown

```text
self.client
 ↓
Client Object

call_async(...)
 ↓
method

request
 ↓
Request Object
```

---

# Kya karta hai?

> Request ko asynchronously Service ko send/initiate karta hai aur ek **Future** return karta hai.

```text
Request Object
      ↓
call_async(request)
      ├────────→ Request sent/initiated toward Server
      │
      └────────→ Future returned to Client
```

---

# Important correction

`call_async()`:

❌ Response Object return nahi karta  
❌ server callback nahi hai  
❌ Client callback se Request bhejna zaroori nahi

Returns:

```text
Future
```

See [[Future]].

---

# `async` mental model

Learning me simple intuition:

> Request initiate karo; response aane tak poore program ko unnecessary synchronous wait me freeze karna design requirement nahi.

Exact event processing executor/Future lifecycle ke through hota hai.

---

# Related

- [[Service Client]]
- [[Future]]
- [[Future is not the Response Object]]
