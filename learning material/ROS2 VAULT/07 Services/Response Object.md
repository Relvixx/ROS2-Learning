---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Response Object

Server request process karke output Response Object me prepare karta hai.

---

# Server Callback

```python
def callback(self, request, response):
    response.sum = request.a + request.b
    return response
```

Yahan:

```text
request
→ incoming Request Object

response
→ output Response Object being prepared
```

---

# Example

Input:

```text
request.a = 5
request.b = 7
```

Processing:

```text
5 + 7 = 12
```

Response:

```text
response
└── sum = 12
```

---

# `return response`

Meaning:

> Prepared Response Object ko ROS 2 service mechanism ko wapas dena, taaki response client ko bheja ja sake.

---

# Client side

Python Client me Future complete hone ke baad:

```python
response = future.result()
```

Then:

```python
response.sum
```

actual field value access karta hai.

Important:

```text
Future
≠
Response Object
```

See [[Future is not the Response Object]].

---

# Related

- [[Request Object]]
- [[Server Service Callback]]
- [[Future]]
