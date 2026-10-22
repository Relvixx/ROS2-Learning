---
type: concept
status: locked
depth: must-know
language: Hinglish
canonical: true
---

# Future

Ye concept Services me introduce hua aur Actions me later heavily reuse hua.

---

# Simple definition

> **Future ek asynchronous operation ko represent karta hai jiska actual result baad me available ho sakta hai.**

Service context me:

```text
Future
→ eventual Service Response ka handle/state
```

---

# Creation

```python
future = self.client.call_async(request)
```

Immediately:

```text
Future
┌────────────────────┐
│ result pending     │
└────────────────────┘
```

Server response deta hai.

Then:

```text
Future
┌────────────────────┐
│ completed          │
└────────────────────┘
```

---

# Actual Response kaise milega?

```python
response = future.result()
```

Flow:

```text
Future
   ↓
future.result()
   ↓
Response Object
   ↓
response.sum
```

---

# Future kya nahi hai?

❌ Response Object nahi  
❌ `sum` value nahi  
❌ intelligent checker nahi jo manually server poll karta hai

Better mental model:

> Async operation ka state/handle jise runtime complete karta hai jab result available hota hai.

---

# Service Example

```text
call_async(request)
      ↓
Future
      ↓
Server processes request
      ↓
Response arrives
      ↓
Future completes
      ↓
future.result()
      ↓
Response Object
```

---

# Future Action Connection

Actions me later:

```text
send_goal_future
get_result_future
```

same foundational Future concept reuse hua.

Detailed Actions vault Batch 04 me.

---

# Related

- [[call_async]]
- [[spin_until_future_complete]]
- [[Future is not the Response Object]]
- [[Response Object]]
