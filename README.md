# 🎰 Console Slot Machine

A simple **Python-based slot machine game** that runs in the terminal.
It features weighted reels, a hold mechanic, and a configurable payout system.

---

## 🚀 Features

* 🎲 **Weighted randomness** – symbols appear based on configurable probabilities
* ✋ **Hold mechanic** – lock reels between spins for strategic play
* 💰 **Payout system** – rewards based on symbol combinations
* 🎯 **Configurable settings** – tweak symbols, weights, and payouts easily
* 🧠 **Clean OOP design** – simple and readable class-based implementation

---

## 📸 Screenshots

![Hold/Win Example](screenshots/holdwin.png)
![Lose Example](screenshots/loss.png)

---

## 🕹️ How to Play

1. Run the game
2. The slot machine spins 3 reels
3. After each spin:

   * You can choose reels to **hold** (1–3)
   * Press ENTER to spin again
4. Win based on matching symbols
5. Quit anytime with `q`

---

## 🖥️ Example Gameplay
```
🎰 Welcome to the Slot Machine! 🎰
  ⭐  |  🔔  |  🔔
💵 Wallet: €31.00, 💵 Payout: €0.00, 💵 Session Winnings: €7.00
SPIN #: 13 | Enter reel numbers to (un)hold (1-3, comma-separated), ENTER to spin again, or q to quit:
2,3
Holds remaining: 1
  7️⃣  |[ 🔔 ]|[ 🔔 ]
💵 Wallet: €29.00, 💵 Payout: €0.00, 💵 Session Winnings: €7.00
SPIN #: 14 | Enter reel numbers to (un)hold (1-3, comma-separated), ENTER to spin again, or q to quit:

Holds remaining: 0
  🔔  |[ 🔔 ]|[ 🔔 ]
💵 Wallet: €67.00, 💵 Payout: €40.00, 💵 Session Winnings: €47.00
```

---

## ⚙️ Installation & Running

Clone the repository:

```
git clone https://github.com/starfishgg/slot-machine.git
cd slot-machine
```

Run the game:

```
python slots.py
```

> Requires Python 3.8+

---

## 📁 Project Structure

```
slot-machine/
│
├── main.py        # Entry point (game loop)
├── slots.py       # SlotMachine class
├── app.py         # API Version (Flask Backend)
├── settings.py    # Game configuration (symbols, weights, payouts)
├── screenshots/   # Images for README
└── README.md
```

---

## 🔧 Configuration

All game settings are defined in `settings.py`:
```
SLOT_SYMBOLS = ["🍒", "🍋", "🍊", "🍉", "🔔", "⭐", "7️⃣", "BAR"]
SLOT_WEIGHTS = [30, 20, 20, 15, 8, 4, 2, 1]

SLOT_PAYOUTS = {
    ("7️⃣", 3): 150,
    ("BAR", 3): 100,
    ("⭐", 3): 50,
    ("🔔", 3): 25,
    ("🍒", 3): 10,
    ("🍒", 2): 5,
}
```

---

## 🧠 Game Logic

* Each reel spins independently using weighted randomness
* Holds allow players to lock reels between spins
* Payouts are determined by:

  * Symbol type
  * Number of matches (2 or 3)
* Only the **highest payout per spin** is awarded

---

## 🌐 API Version (Flask Backend)

This project also includes a simple **Flask API** ('app.py') that exposes the slot machine logic over HTTP.

Instead of playing in the console, you can trigger spins via a web request.

---

### ▶️ Running the API

Install Flask (if not already installed):

```bash
pip install flask
```

Run the server:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

### 🎰 Spin Endpoint

Trigger a spin by visiting:

```
http://127.0.0.1:5000/spin
```

---

### 📦 Example Response

```json
{
  "result": ["🍒", "🍒", "🍒"],
  "payout": 10,
  "win": true,
}
```

---

### 🧠 How It Works

* The API reuses the core `SlotMachine` class from `slots.py`
* All spin logic, weights, and payouts are shared with the console version
* The `/spin` endpoint:

  * Spins all reels
  * Calculates payout
  * Returns the result as JSON

---

### ⚠️ Notes

* The API currently maintains a **single shared game state**
* Each request updates the same slot machine instance
* This is fine for local testing, but not suitable for multi-user environments

---

## 🛠️ Future Improvements

* Link in to my more solid random number generator project
* 🔊 Sound effects
* 🎰 Animated/timed reel-strip implementation
* 
* API Version
* Add endpoints for holding reels to the api version ( /hold )
* Add player sessions (currently only a single shared game state)
* Build a frontend (web UI) to interact with the API

---

## 📜 License

This project is open source and available under the MIT License.

---

## 🙌 Acknowledgements

Built as a learning project to explore:

* Python OOP design
* Randomness and probability
* Game logic implementation
