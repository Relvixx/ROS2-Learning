---
type: correction
status: canonical
language: Hinglish
---

# Future is not the Response Object

## Wrong mental model

```text
call_async()
↓
Response Object
```

❌

---

# Correct

```python
future = self.client.call_async(request)
```

returns:

```text
Future
```

Later:

```python
response = future.result()
```

gives:

```text
Response Object
```

---

# Flow

```text
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

# Why important?

Actions me bhi multiple Futures aate hain.

Agar Service me ye distinction weak ho to Action Client extremely confusing lagta hai.

See [[Future]].
