---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Service Client

Client ka role:

> Request prepare karna aur Service Server ko call/initiate karna.

---

# Conceptual Code Foundation

```python
class AddTwoIntsClient(Node):

    def __init__(self):
        super().__init__('add_two_ints_client')

        self.client = self.create_client(
            AddTwoInts,
            'add_two_ints'
        )
```

---

# Client Flow

```text
Client Object
 ↓
service availability
 ↓
Request Object
 ↓
request fields fill
 ↓
call_async(request)
 ↓
Future
 ↓
response eventually arrives
 ↓
Future complete
 ↓
future.result()
 ↓
Response Object
```

---

# Key concepts

- [[create_client]]
- [[wait_for_service]]
- [[Request Object]]
- [[call_async]]
- [[Future]]
- [[spin_until_future_complete]]
- [[Response Object]]

---

# Important

Service ko fundamentally synchronous mat samjho.

Humne client side:

```python
call_async()
```

study kiya, jo asynchronous request initiate karta hai.
