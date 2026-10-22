---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Request Object

Client Service Server ko jo input bhejta hai, wo Request Object ke structure me hota hai.

---

# Create

```python
request = AddTwoInts.Request()
```

Object:

```text
request
├── a
└── b
```

---

# Fill values

```python
request.a = 5
request.b = 7
```

Now:

```text
request
├── a = 5
└── b = 7
```

---

# Same OOP pattern as Message Object

Publisher:

```python
msg = String()
msg.data = "Hello"
```

Service Client:

```python
request = AddTwoInts.Request()
request.a = 5
request.b = 7
```

Common pattern:

```text
Object
  ↓
Field
  ↓
Value
```

---

# Server side

Server callback receives incoming Request Object:

```python
def callback(self, request, response):
```

Then:

```python
request.a
request.b
```

fields access hote hain.

---

# Request ≠ Response

Request ke fields:

```text
a
b
```

Response field:

```text
sum
```

Separate objects.

See [[Request and Response are Different Objects]].

---

# Related

- [[Service Interface]]
- [[Response Object]]
- [[call_async]]
