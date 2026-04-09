# settings.py

STARTING_CASH = 50
SPIN_COST = 2 # changing this number from 1-3 will dramatically alter the ability to not go broke

# Casino Psychology trick, BAR is rarer, but 7 pays more
SLOT_SYMBOLS = ["🍒", "🍋", "🍊", "🍉", "🔔", "⭐", "7️⃣", "BAR"]
# fair weights, can overwrite with a more gambling style weighted system
# Ironically you will probably lose your money faster with these weights
#  as small wins are less likely (but big wins ALOT more likely if you [HOLD])
SLOT_WEIGHTS = [ 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5] # for testing
# SLOT_WEIGHTS = [ 30, 20, 20, 15, 8, 4, 2, 1] # weighted
SLOT_PAYOUTS = {
    # High-tier (Big 3 of a kind)
    ("7️⃣", 3): 150,   # Jackpot
    ("BAR", 3): 100,   # Casino Psychology trick, BAR is rarer, but 7 pays more
    ("🔔", 3): 40,
    ("⭐", 3): 25,

    # Mid-tier (Big 2 of a kind, no payouts (Casino-style), or small payouts for fun (but less holding))
    ("7️⃣", 2): 0,
    ("BAR", 2): 0,
    ("🔔", 2): 0,
    ("⭐", 2): 0,

    # Low-tier (fruits)
    ("🍒", 3): 10,
    ("🍒", 2): 5,

    ("🍋", 3): 8,
    ("🍋", 2): 3,

    ("🍊", 3): 8,
    ("🍊", 2): 3,

    ("🍉", 3): 6,
    ("🍉", 2): 2
}

SLOT_WHEELS = 3