---
type: object-chain
status: locked
depth: must-know
language: Hinglish
---

# `future.result().result`

Famous confusing line:

```python
result = future.result().result
```

Isko ek saath mat padho.

---

# Step 1

```python
future.result()
```

Completed Result Future se result-response/wrapper object milta hai.

---

# Step 2

```python
future.result().result
```

Wrapper ke andar ka:

```text
result
```

field/property actual Action Result Object deta hai.

---

# Tree

```text
future
 ↓
future.result()
 ↓
Result Response / Wrapper
 └── result
      ↓
   Fibonacci Result Object
      └── sequence
```

---

# Final

```python
result.sequence
```

final Fibonacci sequence field access karta hai.

---

# Why double `.result`?

First `result()`:

```text
Future API method
```

Second `.result`:

```text
returned wrapper ke andar actual Action Result field
```

Same word, different levels.

---

# Related
- [[Action Result Object]]
- [[Future]]
