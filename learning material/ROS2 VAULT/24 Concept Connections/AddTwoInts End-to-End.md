---
type: connection-map
status: locked
language: Hinglish
---

# AddTwoInts End-to-End

Batch 03 ka master connection map.

---

# Interface

```text
example_interfaces/srv/AddTwoInts

Request:
int64 a
int64 b

---

Response:
int64 sum
```

---

# Client Objects

```text
Client Node
└── Client Object
      ↓
   Request Object
      ├── a = 5
      └── b = 7
```

Client action:

```python
future = self.client.call_async(request)
```

---

# Runtime

```text
Request Object
a=5, b=7
     ↓
call_async()
     ↓
Future returned
     │
     │ Request
     ▼
/add_two_ints
     ↓
Server Node
     ↓
callback(request, response)
     ↓
response.sum = 5 + 7
     ↓
Response Object
sum=12
     │
     │ Response
     ▼
Client Runtime
     ↓
Future complete
     ↓
future.result()
     ↓
Response Object
     ↓
response.sum
     ↓
12
```

---

# CLI version

```bash
ros2 service call /add_two_ints \
example_interfaces/srv/AddTwoInts \
"{a: 5, b: 7}"
```

CLI automatically Request Object preparation/sending handle karta hai.

Verified output:

```text
AddTwoInts_Request(a=5, b=7)
AddTwoInts_Response(sum=12)
```

---

# Core Relationships

```text
Interface
 ↓
Request Type + Response Type

Request Type
 ↓
Request Object

Response Type
 ↓
Response Object

Client Object
 ↓
call_async(Request)
 ↓
Future

Server callback
 ↓
Response preparation

Future complete
 ↓
future.result()
 ↓
Response Object
```

---

# Next Connection

Actions me Service ke concepts reuse honge:

```text
async
Future
callback
interface
client/server thinking
```

Lekin Actions me extra:

```text
Goal
Feedback
Result
Goal Handle
```

Detailed next batch me.
