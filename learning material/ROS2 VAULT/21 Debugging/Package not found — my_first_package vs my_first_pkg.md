---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Package not found — `my_first_package` vs `my_first_pkg`

## Symptom

Command:

```bash
ros2 run my_first_package publisher_node
```

Error:

```text
Package 'my_first_package' not found
```

Subscriber ke saath bhi same wrong package name try hua.

---

# Evidence

CLI:

```bash
ros2 pkg executables my_first_pkg
```

me executables actually visible the:

```text
my_first_pkg publisher_node
my_first_pkg subscriber_node
...
```

---

# Root Cause

Actual ROS package name:

```text
my_first_pkg
```

Use kiya gaya wrong name:

```text
my_first_package
```

---

# Fix

```bash
ros2 run my_first_pkg publisher_node
```

and:

```bash
ros2 run my_first_pkg subscriber_node
```

---

# Verification

Publisher:

```text
Hello from ROS2
```

Subscriber:

```text
Hello from ROS2
```

both run hue.

---

# Prevention

Command se pehle exact installed package verify:

```bash
ros2 pkg list | grep my_first
```

ya:

```bash
ros2 pkg executables my_first_pkg
```

---

# Engineering lesson

> Folder/project ka assumed naam nahi — ROS package ka actual registered name use karo.

See [[Package and Executable]].
