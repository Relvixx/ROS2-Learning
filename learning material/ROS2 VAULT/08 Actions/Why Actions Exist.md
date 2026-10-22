---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Why Actions Exist

Services ke baad question tha:

> Agar task turant complete nahi hota aur hume beech-beech me progress bhi chahiye to?

Examples:

```text
Robot ko destination tak le jaana
Arm ko long motion execute karna
Navigation
Long computation
```

Sirf ek Request → Response mental model progress ko naturally express nahi karta.

Action pattern me:

```text
Goal
 ↓
Execution
 ↓
Feedback
 ↓
Feedback
 ↓
Final Result
```

---

# Simple definition

> **Action goal-based communication pattern hai jo longer-running task ke liye Goal, intermediate Feedback aur final Result provide karta hai.**

---

# Core 3 Parts

```text
Goal
→ kya task karna hai

Feedback
→ task ke beech progress kya hai

Result
→ final output kya mila
```

---

# Fibonacci example

```text
Goal:
order = 6

Feedback:
[0,1]
[0,1,1]
[0,1,1,2]
...

Result:
[0,1,1,2,3,5]
```

---

# Topic / Service connection

```text
Topic
→ publish/subscribe messages

Service
→ request/response

Action
→ goal + progress feedback + final result
```

See [[Topic vs Service vs Action]].
