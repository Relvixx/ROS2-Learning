---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# `goal_handle.succeed()`

Server:

```python
goal_handle.succeed()
```

Meaning:

> Goal execution ko successful terminal state me mark karo.

---

# Correct order

```text
Execution
 ↓
Feedback / processing
 ↓
Task actually complete
 ↓
succeed()
 ↓
Result prepare/return
```

---

# Why important?

Historical quiz me ye explicitly discussed hua:

Agar `succeed()` tak execution nahi pahunchta, Goal successful mark nahi hota.

Actual overflow error run me:

```text
execute_callback crash
 ↓
succeed() reached nahi
 ↓
Goal state success set nahi
 ↓
goal aborted behavior observed
```

See [[Action Fixed Width Integer Overflow]].

---

# Important refinement

"succeed() na ho to client forever wait karega" early simplification thi.

Vault ka safer mental model:

> Server ko goal terminal state correctly set karni hoti hai; successful execution ke liye `succeed()` relevant hai. Callback error me framework ne goal ko aborted state assume kiya tha.
