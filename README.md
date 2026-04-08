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

Place your images inside a `/screenshots` folder in your repo.

```id="o3i2nx"
slot-machine/
├── screenshots/
│   ├── holdwin.png
│   └── loss.png
```

### Example

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
git clone https://github.com/your-username/slot-machine.git
cd slot-machine
```

Run the game:

```
python slots.py
```

> Requires Python 3.8+

---

## 📁 Project Structure


slot-machine/
│
├── main.py        # Entry point (game loop)
├── slots.py       # SlotMachine class
├── settings.py    # Game configuration (symbols, weights, payouts)
├── screenshots/   # Images for README
└── README.md
```

---

## 🔧 Configuration

All game settings are defined in `settings.py`:

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

## 🛠️ Future Improvements

* Link in to my more solid random number generator project
* 🎨 GUI version (Tkinter/Pygame or web-based)
* 🔊 Sound effects
* 🎰 Animated/timed reel-strip implementation

---

## 📜 License

This project is open source and available under the MIT License.

---

## 🙌 Acknowledgements

Built as a learning project to explore:

* Python OOP design
* Randomness and probability
* Game logic implementation
