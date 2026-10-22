---
type: debugging-model
status: verified
depth: must-know
language: Hinglish
---

# Launch Success vs Node Runtime Success

Multi-node practical me important lesson:

```text
Launch system
→ publisher process start ✅
→ subscriber process start ✅

Then:
publisher Python code crashed ❌
subscriber kept running ✅
```

---

# Meaning

> Launch action successfully process start kar sakta hai, lekin launched program apne internal runtime bug ki wajah se later crash kar sakta hai.

So layers separate:

```text
Launch layer
 ↓
process start

Application/Python layer
 ↓
program execution
```

A launch error aur node code error same cheez nahi.

See [[Publisher Crashed After Successful Launch]].
