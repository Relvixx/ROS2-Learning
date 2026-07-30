# ROS2 Core Foundations — Meri Revision Notes
### (Nodes → Publisher/Subscriber → CLI Tools → Services)
**System:** Ubuntu 24.04 (Noble) + ROS2 Jazzy | **Workspace:** `~/ros2_jazzy` | **Package:** `my_first_pkg`

---

## 0. SETUP — jo pehle kiya (yaad rakhne wali cheezein)

- **Ubuntu 24.04 → sirf ROS2 Jazzy chalega** (Humble sirf 22.04 ke liye hai — yeh galti nahi doharaani)
- Shell **zsh** hai, isliye hamesha `setup.zsh` use karna, `setup.bash` NAHI
  ```bash
  source /opt/ros/jazzy/setup.zsh
  source ~/ros2_jazzy/install/setup.zsh
  ```
- **Har naye terminal mein source karna padta hai** — jab tak `.zshrc` mein permanently add na ho
- **Workspace ka sahi structure:**
  ```
  ~/ros2_jazzy/
  ├── src/            ← packages YAHAN bante hain (yeh bhoolna nahi — mainne ek baar galti se bahar bana diya tha)
  ├── build/           ← colcon build se auto-generate
  ├── install/         ← colcon build se auto-generate (final ready-to-use version)
  └── log/             ← colcon build se auto-generate
  ```
- **`build/install/log` VS Code explorer mein nahi dikhte** — yeh normal hai, feature hai bug nahi (auto-generated cheezon ko chhupa dete hain)

---

## 1. PACKAGE KYA HAI (Almirah wali analogy)

> **Package = ek self-contained folder jisme robotics-related code organized tarike se rehta hai, taaki ROS2 ko pata ho yeh kya hai aur kaise chalana hai.**

**Kyun banate hain:** Agar saara code ek hi jagah daal do, dhundhna mushkil, reuse karna mushkil, team mein kaam karna mushkil. Isliye har kaam (vision, motor, sensor) ka apna alag package banate hain.

### Banane ka command
```bash
cd ~/ros2_jazzy/src        # ⚠️ SRC KE ANDAR HONA ZAROORI HAI
ros2 pkg create my_first_pkg --build-type ament_python --dependencies rclpy
```

### Command ka breakdown
| Part | Matlab |
|---|---|
| `ros2 pkg create` | naya package banao |
| `my_first_pkg` | package ka naam |
| `--build-type ament_python` | Python code ke liye (C++ ke liye `ament_cmake`) |
| `--dependencies rclpy` | isko `rclpy` library chahiye hi chahiye |

### Andar kya banta hai — file by file
| File/Folder | Kya hai | Analogy |
|---|---|---|
| `package.xml` | Naam, version, dependencies, license — package ka "identity card" | Aadhar card |
| `setup.py` | Build/install kaise karna hai, kaunse files "executable" hain | Recipe card |
| `setup.cfg` | `setup.py` ka chhota helper | — |
| `my_first_pkg/` (andar wala, same naam) | **Yahan asli Python code (nodes) likhte hain** | Khaali shelf jahan saman rakhoge |
| `my_first_pkg/__init__.py` | Khaali file, Python ko batati hai "yeh ek package hai" | — |
| `resource/` | ROS2 ko "yeh valid package hai" batane wala marker | Registration certificate |
| `test/` | Automated code-quality checks (`flake8`, `pep257`, copyright) | — |

---

## 2. `colcon build` aur `source` — YEH DONO KYUN CHALATE HAIN

**Analogy: Naya restaurant khola**
1. Building bana li (`package.xml`, `setup.py` likh diya) → abhi operational nahi
2. **`colcon build`** = construction complete karna (electricity, kitchen set karna) → `build/` aur `install/` folders banata hai, code ko **compile/ready** karta hai
3. **`source install/setup.zsh`** = Google Maps pe register karna → terminal ko batata hai "yeh naya package available hai, use kar sakte ho"

⚠️ **`source` HAR NAYE TERMINAL mein karna padta hai** — kyunki naya terminal by default sirf system-wide ROS2 janta hai, tumhare custom workspace ke baare mein nahi.

### Command pattern
```bash
cd ~/ros2_jazzy
colcon build --packages-select my_first_pkg    # sirf ek package build karo (poore workspace se fast)
source install/setup.zsh
```

### Common error jo face kiya: cache issue
Agar code sahi hone ke baad bhi `no attribute 'main'` jaisa error aaye → **clean rebuild karo**:
```bash
rm -rf build/my_first_pkg install/my_first_pkg log
colcon build --packages-select my_first_pkg
```

---

## 3. NODE KYA HAI

> **Node = ek independent chhota program jo ek specific kaam karta hai, aur zaroorat pe doosre nodes se "baat" kar sakta hai.**

**Analogy:** Ghar mein cook, cleaner, guard — alag-alag insaan, apna-apna kaam independently karte hain, zaroorat pe baat karte hain.

### Sabse simple node — template (BOILERPLATE, roz naya nahi likhna)
```python
import rclpy
from rclpy.node import Node


class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        self.get_logger().info('Simple node is running!')


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

### ⭐ MERA BADA DAR THA: "kya roz itna complex code likhna padega?"
**Jawab: NAHI.** Yeh code **boilerplate** hai — jaise ek email template jisme sirf "Dear [Naam]" wala naam badalta hai. Har node mein sirf **3 jagah naam badalta hai**:
1. `class SimpleNode(Node):` → class ka naam
2. `super().__init__('simple_node')` → node ka naam
3. `node = SimpleNode()` → wahi class naam

Baaki poora structure (`main()`, `rclpy.init`, `spin`, `shutdown`, `if __name__==...`) **hamesha same rehta hai, copy-paste karte hain.**

### Execution ka EXACT order (line-by-line trace)
```
1. rclpy.init()              → ROS2 "ON" hota hai
2. node = SimpleNode()       → Node banta hai
      ├─ super().__init__()  → naam register hota hai
      └─ get_logger().info() → yahan "running!" print hota hai
3. rclpy.spin(node)          → YAHAN RUK JAATA HAI (jab tak Ctrl+C na ho)
   ... Ctrl+C dabaya ...
4. node.destroy_node()       → node delete
5. rclpy.shutdown()          → ROS2 "OFF"
```

### ⭐ MERA QUIZ JAWAB (sahi tha): `rclpy.spin(node)` hata do toh?
**"Program turant band ho jayega"** — Correct! Kyunki Python line-by-line chalta hai, `spin()` hi hai jo "yahan ruko" bolta hai. Bina iske, node banega, ek line print karega, aur turant `destroy_node()` + `shutdown()` chal jayenge.

### Node ko "chalane layak" banane ke 2 ZAROORI steps
1. **Executable banao:**
   ```bash
   chmod +x path/to/file.py
   ```
2. **`setup.py` mein entry point register karo:**
   ```python
   entry_points={
       'console_scripts': [
           'simple_node = my_first_pkg.simple_node:main',
       ],
   },
   ```
   Pattern: `'<terminal_command_naam> = <package>.<file>:main'` — "jab yeh naam terminal mein type ho, toh yeh file ka `main` function chalao." Yeh **address book entry jaisi hai** — ek baar likhi, hamesha kaam karegi. Har naye node ke liye ek nayi line add karni padti hai (yeh zaroori hai, skip nahi kar sakte).

### Run karne ka command
```bash
ros2 run my_first_pkg simple_node
```

### Node ka pura "tools kit" — `Node` class kya deti hai (inheritance se)
Jab `class X(Node):` likha, **automatically yeh sab tools mil gaye** bina khud banaye:
| Method | Kaam | Kab use hota hai |
|---|---|---|
| `self.get_logger().info()` | Print karna | Hamesha |
| `self.create_publisher()` | Broadcast channel banana | Publisher mein |
| `self.create_subscription()` | Channel sunna | Subscriber mein |
| `self.create_timer()` | Automatic repeat karne wala alarm | Publisher mein |
| `self.create_service()` | Request-response system | Service Server mein |
| `self.create_client()` | Service ko call karna | Service Client mein |

**Yaad rakhne ka tarika:** Goal decide karta hai method — "data bhejna hai?" → publisher. "Data sunna hai?" → subscription. "Baar-baar automatic kuch karna hai?" → timer. Yeh pattern practice se yaad ho jaata hai, sab kuch memorize karne ki zaroorat nahi.

---

## 4. TOPICS — Publisher aur Subscriber (Continuous, One-Way)

**Analogy: Radio Station** — Publisher = radio station (broadcast karta rehta hai chahe koi sune ya na sune). Subscriber = radio jo tune karke sunta hai. Dono **ek doosre ko directly nahi jaante**, sirf topic-naam se connect hote hain. Yehi hai **"decoupling"** — ROS2 ka sabse powerful idea.

### PUBLISHER — poora code
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        message = String()
        message.data = 'Hello from ROS2'
        self.publisher_.publish(message)
        self.get_logger().info(message.data)


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

### Naye 4 concepts (baaki sab SimpleNode jaisa hi hai)

**1. `from std_msgs.msg import String`**
"Envelope" ka type — batata hai kis format mein data bhejenge (yahan: sirf text). Aage `Float32`, `Int32`, `Image` jaise doosre bhi milenge.

**2. `self.create_publisher(String, 'hello_topic', 10)`**
```
create_publisher( String,   'hello_topic',   10 )
                    ↑             ↑           ↑
              kya bhejenge   channel naam   queue size
              (format)       (khud choose    (slow subscriber
                              karte ho)       ke liye buffer)
```
**Analogy:** "Main ek nayi radio frequency start kar raha hoon naam `hello_topic`, isme text broadcast karunga."

**3. `self.create_timer(1.0, self.timer_callback)`**
Alarm — "har 1.0 second baad `timer_callback` khud-ba-khud chalao."

**4. `timer_callback()` function — publish karne ke 4 steps**
```python
message = String()                    # A: khaali envelope banao
message.data = 'Hello from ROS2'      # B: envelope mein text daalo
self.publisher_.publish(message)      # C: bhej do
self.get_logger().info(message.data)  # D: khud dekhne ke liye print
```

### ⭐ MERA DOUBT (mixup): Topic naam vs Message content
Yeh **do bilkul alag cheezein** hain, dono text jaisi dikhti hain isliye confuse hua tha:

| Cheez | Kya hai | Kahan likha jaata hai |
|---|---|---|
| **Topic naam** | Kis channel pe bhej rahe ho | `create_publisher(String, 'YAHAN', 10)` |
| **Message content** | Kya text bhej rahe ho | `message.data = 'YAHAN'` |

**Analogy:** WhatsApp group ka naam = `'Family Group'` (topic), group mein likha message = `'Aaj dinner 8 baje'` (message.data). Dono text hain, lekin kaam bilkul alag.

### ⭐ MERA SAWAAL: Kya publish HAMESHA `timer_callback` ke andar hi hota hai?
**Nahi.** `self.publisher_.publish(message)` **kisi bhi function ke andar** likh sakte ho jo call ho:
- **Timer se** (regular interval — sensor reading har second)
- **Event se** (jaise button-press function ke andar — sirf jab kuch ho tabhi)
- **`__init__` mein ek baar** (jaise "node start ho gaya" announcement)

Timer sirf **ek choice** thi humare use-case (repeat karna) ke liye — rule nahi.

### SUBSCRIBER — poora code
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'hello_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

**Key points:**
- `String` aur `'hello_topic'` **exactly match** hone chahiye publisher se — warna dono ek doosre ko "sun" nahi payenge (jaise radio frequency match na ho)
- `listener_callback` **timer se nahi**, balki **automatically chalta hai jab bhi naya message aaye** — yeh subscriber aur publisher ka bada structural fark hai
- `msg` parameter mein poora message aata hai, `msg.data` se content nikaalte hain

### ⭐ MERA SAWAAL: Kya topic sirf ek subscriber ke liye banta hai?
**Nahi.** Topic **kisi ke liye bhi** hota hai jo sunna chahe:
- Publisher chalta rehta hai **chahe subscriber ho ya na ho** (`Subscription count: 0` bhi valid state hai)
- **Ek se zyada subscribers** ho sakte hain ek hi topic pe (jaise ek YouTube video lakhon log dekh sakte hain)
- Publisher ko **kabhi pata nahi chalta** kitne subscribers hain — yehi hai "decoupling"

### Verify karne ke commands (isse pata chalta hai sach mein data ja raha hai, sirf print nahi ho raha)
```bash
ros2 topic list                    # /hello_topic dikhna chahiye
ros2 topic info /hello_topic       # Type, Publisher count, Subscription count
ros2 topic echo /hello_topic       # live data dekho
```

---

## 5. TOPIC CLI TOOLS — Debugging ke liye (naya code nahi, sirf existing tools)

**Kyun important:** Real robot mein 10+ nodes chalte hain, koi problem ho toh **har code padhna nahi padta** — yeh tools se pata chal jaata hai.

| Command | Kya karta hai |
|---|---|
| `ros2 topic list` | Kaunse topics chal rahe hain |
| `ros2 topic info /topic_naam` | Message type, publisher/subscriber count |
| `ros2 topic echo /topic_naam` | Live data dekhna |
| `ros2 topic hz /topic_naam` | Kitni frequency (Hz) se message aa rahe hain — timing issue pakadne ke liye |
| `ros2 topic pub /topic_naam TYPE "data"` | **Bina code likhe** terminal se hi message publish karna (testing ke liye) |
| `ros2 topic pub -r 2 /topic_naam TYPE "data"` | Repeated publish, `-r 2` = 2 Hz rate se |

**Note:** `ros2 topic hz` ko band karne ke liye **`Ctrl+C`** use karo, `Ctrl+Z` sirf "suspend/pause" karta hai (background mein chalta rehta hai) — agar `Ctrl+Z` use kiya toh `kill %1` se poora band karo.

**Important insight:** `ros2 topic pub` se manually bheja gaya data aur asli publisher node ka data — dono **ek saath ek hi topic pe** chal sakte hain, ROS2 ko koi fark nahi padta data kahan se aaya. **"Topics don't care where messages come from."**

---

## 6. SERVICES — Request-Response (Synchronous, Do-Tarfa)

**Topic vs Service — core fark:**

| | Topic | Service |
|---|---|---|
| Direction | Ek-tarfa continuous | Do-tarfa, ek baar |
| Kab use karo | Continuous data (sensor, camera) | Ek specific sawaal-jawab (battery %, status check) |
| Roles | Publisher + Subscriber | Server + Client |
| Wait karna | Nahi | Haan — client response ka wait karta hai (**synchronous**) |

**Analogy: Restaurant Waiter**
- Tum order dete ho ("pizza dena") = **Request**
- Tum table pe wait karte ho jab tak pizza na aaye = **synchronous**
- Waiter laata hai = **Response**
- Baat khatam — koi continuous streaming nahi

### SERVER — poora code
```python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_two_ints_callback
        )

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Request: {request.a} + {request.b} = {response.sum}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

**Naye concepts:**
- **`AddTwoInts`** = built-in service type jisme **do hisse** hote hain: Request (`a`, `b`) + Response (`sum`) — Topic mein sirf ek envelope tha, yahan **do envelope** (jaane wala + aane wala)
- **`add_two_ints_callback(self, request, response)`** — automatically chalta hai jab client request bheje. **Subscriber ke callback se bada fark: yeh function `response` HAMESHA RETURN karta hai** (kyunki client wait kar raha hai)

### CLIENT — poora code
```python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        self.future = self.cli.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.send_request(5, 7)
    rclpy.spin_until_future_complete(node, node.future)
    response = node.future.result()
    node.get_logger().info(f'Result: {response.sum}')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

**Naye concepts:**
- `wait_for_service()` — server available hai ya nahi, pehle check
- `request = AddTwoInts.Request()` — khaali "order form"
- `self.future = self.cli.call_async(request)` — request bheji, **turant jawab nahi milta**, `future` mein "aayega toh yahan store hoga"
- `rclpy.spin_until_future_complete(node, node.future)` — **yehi hai "wait karo jab tak jawab na aaye"** wala part

### Poora flow
```
1. Server start        → "ready hoon, requests suno"
2. Client request bhejta → a=5, b=7
3. Server callback chalta → 5+7 calculate
4. Server response bhejta → sum=12
5. Client wait karke jawab leta → print "Result: 12"
```

### CLI se bhi test kar sakte ho (bina client code likhe)
```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5, b: 7}"
```

### ⭐ MERA REAL DOUBT: Faced Build Error
`AttributeError: module '...' has no attribute 'main'` — jabki code mein `def main` sahi likha tha. **Reason: build cache purana version rakhe hue tha.** Fix:
```bash
rm -rf build/my_first_pkg install/my_first_pkg log
colcon build --packages-select my_first_pkg
```
**Sabak:** Agar code sahi hone ke baad bhi weird error aaye jo "impossible" lage, **pehle clean rebuild try karo.**

### ⭐ MERA SAWAAL: Built-in vs Custom Services
- **Built-in** (`AddTwoInts`, `SetBool`, `Trigger` from `example_interfaces`/`std_srvs`) = sirf **practice/demo** ke liye
- **Real projects mein khud ki custom `.srv` file banate ho** — apne specific request/response fields define karke (yeh "Actions with Separate Interface Package" lecture mein aayega)

### Real Industry Example — kab Service use hota hai
**Warehouse robot scenario:** `task_manager_node` naya task lene se pehle `battery_monitor_node` ko **service call** karta hai: "kya 20% battery kaafi hai?" → turant `sufficient: true/false` jawab milta hai. Agar `false`, robot charging station bhejta hai, task shuru nahi karta.

**Yeh Service kyun, Topic nahi:** Yeh **ek specific decision point** hai (continuous nahi), aur **turant confirmation** chahiye — task_manager agla step tabhi lega jab jawab mil jaye. Topic hota toh continuous stream se filter karna padta, messy hota.

**Decision rule (yaad rakhna):**
> "Continuous stream chahiye?" → **Topic**
> "Ek sawaal, turant confirm jawab chahiye?" → **Service**

Examples: Camera feed = Topic | Sensor reading har second = Topic | "Battery kaafi hai?" = Service | "Object uthao, confirm karo" = Service | "Motor emergency stop karo" = Service

---

## 7. QUICK COMMAND CHEAT-SHEET (roz kaam aane wale)

```bash
# Naya package
cd ~/ros2_jazzy/src
ros2 pkg create <pkg_name> --build-type ament_python --dependencies rclpy

# File ko executable banana
chmod +x path/to/file.py

# Build
cd ~/ros2_jazzy
colcon build --packages-select <pkg_name>
source install/setup.zsh

# Clean rebuild (agar weird error aaye)
rm -rf build/<pkg_name> install/<pkg_name> log
colcon build --packages-select <pkg_name>

# Node chalana
ros2 run <pkg_name> <node_name>

# Topic debugging
ros2 topic list
ros2 topic info /topic_name
ros2 topic echo /topic_name
ros2 topic hz /topic_name
ros2 topic pub /topic_name TYPE "data"

# Service debugging
ros2 service call /service_name TYPE "{field: value}"
```

---

## 8. MERI OVERALL PROGRESS — Section Complete ✅

```
✅ Node banana + samajhna (lifecycle: init → spin → shutdown)
✅ Publisher banana (create_publisher, create_timer, publish)
✅ Subscriber banana (create_subscription, callback-on-event)
✅ Topic CLI tools (list, info, echo, hz, pub) — debugging skills
✅ Service Server + Client (create_service, create_client, request/response, async+future)
✅ 3 tareekon se verify karna: apna code, CLI tool, aur dusra node
```

**Agla section:** Advanced ROS2 Communication — Actions, Parameters, Launch Files.

---

## 9. MERE APNE GALTIYON KA RECORD (in se seekha)

1. **Package `src/` ke bahar bana diya tha** — `ros2 pkg create` hamesha `src/` folder ke andar se chalana, warna colcon isse dhundh nahi payega
2. **`setup.bash` vs `setup.zsh`** — zsh use karne ki wajah se hamesha `.zsh` wala version use karna, warna `no such file or directory` error aata hai
3. **Motor speed example copy karke temperature banate waqt `m/s` unit reh gaya tha** — jab bhi ek code se doosra banao (copy-paste), **har detail dhyan se check karo**, sirf naam nahi
4. **Topic naam aur message content mix kar diya tha** — dono "text" jaise lagte hain lekin unka role bilkul alag hai
5. **Build cache ka purana version issue** — sahi code likhne ke baad bhi error aaya, `rm -rf build/ install/ log` se clean rebuild ne fix kiya
