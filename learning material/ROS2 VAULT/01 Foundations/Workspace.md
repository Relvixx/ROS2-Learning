---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Workspace

## Simple meaning

Workspace ROS 2 packages ko organize, build aur run karne ke liye main working directory hai.

Hamare learning workspace ka example:

```text
~/ros2_jazzy
```

---

# Structure

```text
~/ros2_jazzy/
├── src/
├── build/
├── install/
└── log/
```

## `src/`

Yahan source packages rehte hain.

Example:

```text
src/
├── my_first_pkg/
└── my_first_interfaces/
```

## `build/`

`colcon build` ke during generated/intermediate build artifacts.

## `install/`

Build ke baad installed package outputs.

ROS environment ko workspace ke packages discover karwane ke liye hum installation environment source karte hain.

Hamare shell ke liye:

```zsh
source install/setup.zsh
```

## `log/`

Build process se related logs.

---

# Workflow

```text
Code likho
   ↓
src/
   ↓
colcon build
   ↓
install/
   ↓
source install/setup.zsh
   ↓
ros2 run ...
```

---

# Important historical debugging lesson

Ek time `src/` ke andar galti se build kiya gaya tha, jisse:

```text
src/build
src/install
src/log
```

bhi create ho gaye the.

Ideal workspace me main build/install/log workspace root par hote hain.

---

# `colcon` ke baare me correction

`colcon` ko "compiler" samajhna exact nahi hai.

Better model:

> `colcon` ROS 2 workspace packages ko orchestrate/build karne wala build tool hai.

Python package me traditional C++ compilation nahi hoti, lekin package preparation/install process phir bhi hota hai.

---

# Related

- [[ROS 2 Ecosystem]]
- [[Package and Executable]]
- [[Node Runtime Flow]]
