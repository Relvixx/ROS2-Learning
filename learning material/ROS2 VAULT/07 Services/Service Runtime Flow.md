---
type: runtime-flow
status: locked
depth: must-know
language: Hinglish
---

# Service Runtime Flow

Master Service story:

```text
SERVICE INTERFACE
Request + Response structure
       ↓

CLIENT
       ↓
Request Object create
       ↓
request.a = 5
request.b = 7
       ↓
call_async(request)
       ↓
Future returned
       │
       │ Request
       ▼
SERVER
       ↓
callback(request, response)
       ↓
response.sum = request.a + request.b
       ↓
return response
       │
       │ Response
       ▼
CLIENT RUNTIME
       ↓
Future completes
       ↓
future.result()
       ↓
Response Object
       ↓
response.sum = 12
```

---

# Object View

```text
AddTwoInts Interface
├── Request type
│     └── Request Object
│          ├── a
│          └── b
│
└── Response type
      └── Response Object
           └── sum
```

---

# Client side

```text
create_client()
 ↓
Client Object
 ↓
call_async(Request Object)
 ↓
Future
```

---

# Server side

```text
create_service()
 ↓
Service registered
 ↓
Request event
 ↓
server callback
 ↓
Response Object prepared
 ↓
return
```

---

# Related

- [[AddTwoInts End-to-End]]
- [[Service Client]]
- [[Service Server]]
- [[Future]]
