---
type: correction
status: canonical
language: Hinglish
---

# Rejected Parameter Keeps Old Valid Value

Actual:

```text
current max_speed = 3.5
request           = 8.0
```

Callback:

```text
8.0 > 5.0
→ reject
```

Then get:

```text
Double value is: 3.5
```

So:

```text
proposed value
≠
stored value until accepted
```
