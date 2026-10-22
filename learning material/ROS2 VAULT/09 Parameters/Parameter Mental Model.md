---
type: mental-model
status: verified
depth: must-know
language: Hinglish
---

# Parameter Mental Model

## Basic picture

```text
ROS Node
└── Parameter
      ├── Name
      ├── Value
      └── Type
```

Example:

```text
/parameter_node
└── max_speed
      ├── name  = max_speed
      ├── value = 2.0
      └── type  = double
```

---

# Lifecycle at current learning level

```text
Node starts
 ↓
declare_parameter()
 ↓
Parameter exists with default/configured value
 ↓
get_parameter()
 ↓
Node reads it
 ↓
CLI can inspect it
 ↓
CLI may set a new value
 ↓
new stored parameter value
```

Validation layer is next chapter.

---

# Configuration idea

```text
Code
≠
Configuration
```

Code says:

```text
"there is a parameter named max_speed"
```

Configuration decides:

```text
"what value should max_speed have for this run?"
```

---

# Three important sources of value

```text
Code default
Launch/startup override
Runtime CLI change
```

See [[Parameter Configuration Paths]].
