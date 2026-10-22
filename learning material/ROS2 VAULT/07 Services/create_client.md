---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `create_client()`

Core:

```python
self.client = self.create_client(
    AddTwoInts,
    'add_two_ints'
)
```

---

# Kya hai?

✅ `Node` ka method.

Returns:

> Client Object / Client handle

---

# Pattern Recognition

```text
create_publisher()
→ self.publisher

create_subscription()
→ self.subscription

create_service()
→ self.service

create_client()
→ self.client
```

---

# Arguments

```text
AddTwoInts
→ Service Type / Interface

'add_two_ints'
→ Service Name
```

Meaning:

> Client ko batana hai kis interface/type ki, kis naam wali Service se baat karni hai.

---

# Object Tree

```text
Client Node Object
└── self.client
      ↓
   Client Object
```

---

# Related

- [[Service Client]]
- [[call_async]]
- [[Service Interface]]
