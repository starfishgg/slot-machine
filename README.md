# 🎰 Python Slot Machine

A fully custom terminal-based slot machine built in Python featuring weighted reels, hold mechanics, payout logic, and statistical simulation tools.

---

## Features

- 🎲 **Weighted Reel System**  
  Customisable reel weights allow realistic probability balancing and RTP tuning.

- 🔒 **Hold Mechanic**  
  Players can hold reels strategically between spins, with anti-abuse logic to prevent infinite hold exploitation.

- 💰 **Dynamic Payout System**  
  Symbol-based payout table supporting:
  - Low-tier fruit payouts for 2+ matches
  - High-tier jackpot symbols requiring 3 matches

- 📊 **Monte Carlo Analysis Tool**  
  Includes simulation engine to analyse:
  - RTP (Return To Player)
  - Win Rate / Hit Rate
  - Symbol Frequency Distribution
  - RTP Contribution by Win Type

- 🌐 **Flask API Backend**
  Experimental backend endpoints for integrating slot spins into web applications.

---

## Project Structure

```bash
slot-machine/
│
├── slots.py        # Main slot machine gameplay logic
├── settings.py     # Configurable weights, symbols and payout tables
├── analysis.py     # Statistical simulation / RTP analysis tool
├── app.py          # Flask API backend prototype
└── screenshots/    # Gameplay + analysis screenshots
```

---

## Recent Updates

### Codebase Improvements
- Refactored `slots.py` to improve readability and separate gameplay logic more cleanly.
- Improved hold-state management and win-condition tracking.
- Added better structured helper methods for payout / win checking.

### Probability Balancing
- Reworked reel weighting values in `settings.py` for more realistic slot odds and smoother RTP balancing.

### Statistical Analysis
- Added `analysis.py` Monte Carlo simulator for 100,000+ spin statistical testing.
- Tracks:
  - RTP %
  - Hit Rate %
  - Total Symbol Frequencies
  - Win Condition Frequencies
  - RTP Contribution Per Win Type

---

## Screenshots

### Gameplay Example
![Gameplay Screenshot](screenshots/holdwin.png)
![Gameplay Screenshot 2](screenshots/loss.png)

### Statistical Analysis Output
![Analysis Screenshot](screenshots/analysis.png)

---

## Example Analysis Output

```bash
📊 SLOT MACHINE ANALYSIS
Spins Simulated: 100,000
Total Wagered: €500,000
Total Paid Out: €456,200
RTP: 91.24%
Win Rate: 27.31%

🍒 x2: 12,431 wins | 12.43% Hit Rate | 4.97% RTP Contribution
🍒 x3: 3,114 wins | 3.11% Hit Rate | 2.49% RTP Contribution
7️⃣ x3: 53 wins | 0.05% Hit Rate | 7.95% RTP Contribution
```

---

## 🛠️ Future Improvements

* Link in to my more solid random number generator project
* Compare RTP Results to Expected Results
* 🔊 Sound effects
* 🎰 Animated/timed reel-strip implementation
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
