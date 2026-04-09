# app.py
# Simple backend API version of the SlotMachine. No hold functionality or or tracking cashflows.

# To run:
# python app.py
# Access the URL: http://127.0.0.1:5000/spin
# Refresh the page for a new spin


from flask import Flask, jsonify # for API version
from settings import SLOT_SYMBOLS, SLOT_WEIGHTS, SLOT_PAYOUTS, STARTING_CASH, SPIN_COST, SLOT_WHEELS
from slots import SlotMachine
import random


app = Flask(__name__)

symbols = SLOT_SYMBOLS
slot = SlotMachine()

def spin_slot():
    slot.spin_all()
    payout = slot.calc_payout()

    return {
        "result": slot.reel_positions,
        "win": payout > 0,
        "payout": payout
    }

@app.route("/spin", methods=["GET"])
def spin():
    return jsonify(spin_slot())




if __name__ == "__main__":
    app.run(debug=True)
