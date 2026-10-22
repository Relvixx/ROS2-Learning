---
type: correction
status: canonical
language: Hinglish
---

# Client does not send Request through Server Callback

Historical explanation me ek point par confusion hua:

> "Client callback function ke through request bhejta hai."

Ye correct nahi.

---

# Correct

Client:

```python
future = self.client.call_async(request)
```

Request initiate/send karta hai.

Server:

```python
def callback(self, request, response):
```

incoming Request ko process karta hai.

---

# Mental Model

```text
CLIENT
call_async(request)
       ↓
       Request
       ↓
SERVER
callback(request, response)
       ↓
process
       ↓
return response
```

---

# Related

- [[call_async]]
- [[Server Service Callback]]
