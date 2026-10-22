---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Action Fixed Width Integer Overflow

## Symptom

Real Action run me server error:

```text
OverflowError: signed integer is greater than maximum
```

Relevant operation:

```python
feedback_msg.partial_sequence.append(...)
```

---

# What had already worked?

Before crash:

```text
Goal sent ✅
Goal accepted ✅
Execution started ✅
Live Feedback received ✅
```

So Action setup itself completely broken nahi tha.

---

# Root Cause Mental Model

Python integer values very large ho sakte hain.

ROS interface field:

```text
int32[]
```

fixed-width integer values expect karta hai.

Fibonacci numbers rapidly grow karte hain.

Eventually:

```text
next Fibonacci value
      ↓
ROS int32 representable range ke bahar
      ↓
serialization / field assignment failure
      ↓
OverflowError
```

---

# Source Inconsistency Correction

Later debugging explanation ne field ko "likely int64[]" bola tha.

Lekin earlier explicit `Fibonacci.action` source definition was:

```text
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

So vault canonical type = **int32**.

Main engineering lesson same:

> Python numeric capability aur ROS fixed-width interface type limit same cheez nahi.

---

# Runtime Consequence

Observed flow:

```text
Goal accepted
 ↓
Feedback
 ↓
Feedback
 ↓
integer too large
 ↓
execute_callback error
 ↓
succeed() reached nahi
 ↓
Goal success state set nahi
```

Framework output indicated goal was treated as aborted.

---

# Fix

Exact code change source me preserve nahi hua.

User later confirmed:

```text
fix kar diya hai
aur sab sahi chal raha hai
```

So resolved status verified, exact patch intentionally invented nahi kiya gaya.

---

# Prevention

- Action/interface numeric types ki bounds yaad rakho.
- Input `order` ko realistic range me validate karna engineering-wise useful hai.
- Large values ke liye interface type design consciously choose karo.
- Python variable large number handle kar leta hai isliye ROS field bhi karega — assume mat karo.

---

# Related
- [[Fibonacci Action Interface]]
- [[LAB 06 — Fibonacci Action Client Runtime]]
