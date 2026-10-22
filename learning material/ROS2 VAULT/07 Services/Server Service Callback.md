---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Server Service Callback

Core callback:

```python
def callback(self, request, response):
    response.sum = request.a + request.b
    return response
```

---

# `request`

Client se aaya hua Request Object.

Example:

```text
request
├── a = 10
└── b = 20
```

---

# `response`

Server ko output prepare karne ke liye milne wala Response Object.

```python
response.sum = 30
```

---

# Full flow

```text
Request Object
a = 10
b = 20
   ↓
callback(request, response)
   ↓
request.a + request.b
   ↓
30
   ↓
response.sum = 30
   ↓
return response
```

---

# Important correction

Client side Request bhejne ke liye server callback use nahi hota.

Correct:

```text
CLIENT
call_async(request)
      ↓
SERVER
callback(request, response)
```

See [[call_async]].

---

# Related

- [[Request Object]]
- [[Response Object]]
- [[Service Server]]
