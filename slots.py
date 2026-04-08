# slots.py
# implementation of SlotMachine class



import random # we can use previously implemented improved random number generator later
from settings import SLOT_SYMBOLS, SLOT_WEIGHTS, SLOT_PAYOUTS, STARTING_CASH, SPIN_COST


class SlotMachine:
    def __init__(self):
        # Symbols and weghts
        self.symbols = SLOT_SYMBOLS
        self.weights = SLOT_WEIGHTS
        self.payouts = SLOT_PAYOUTS
        self.reels = 3
        self.totalpayout = 0
        self.spincost = SPIN_COST
        self.startingmoney = STARTING_CASH
        self.currentmoney = self.startingmoney
        self.lastpayout = 0
        self.allowholds = True
        self.anyholdsactive = False # If this is true, incrememnt the hold count
        self.holdcount = 0 # Don't allow holding more than 1-2 times in a row
        self.maxholdcount = 2
        self.spincount = 0

        # Track the current state of each reel
        self.reel_positions = [None] * self.reels

        # Track held reels (False = spin, True = hold)
        self.held = [False] * self.reels


    # Checks if the specified reel is in a [HOLD] state (returns true/false)
    def is_reel_held(self, index):
        return self.held[index]
    

    # Checks if any of the reels are in a [HOLD] state (returns true/false)
    def any_reels_held(self):
        if self.holdcount >= self.maxholdcount:
            self.reset_holds()
        reels_held = any(self.held)
        if reels_held:
            self.holdcount += 1
            return reels_held
        else:
            return False
        
    

    # Spins a single reel (will be called by spin_all)
    def spin_reel(self, index):
        # Spin a single reel
        if not self.held[index]:
            self.reel_positions[index] = random.choices(
                self.symbols, 
                weights=self.weights, 
                k=1
            )[0]


    # Spins all the reels, calling spin_reel with an index for each one
    def spin_all(self):
        if self.any_reels_held():
            print(f"Holds remaining: {self.maxholdcount-self.holdcount}")
        # Spin all non-held reels
        for i in range(self.reels):
            self.spin_reel(i)
        self.spincount += 1



    # Flip the [HOLD] state of the referenced reel (true to false or false to true, unless you just had a payout - to stop reholding a payout condition)
    def change_hold_reel_state(self, index):
        if 0 <= index < self.reels: # make sure index is between 0 and max reels
            if self.allowholds:
                # Toggle hold on a reel
                # print(f"Changing state of reel {index} from {self.held[index]} to {not self.held[index]}")
                self.held[index] = not self.held[index]
            else:
                print("Holds are not allowed on payout spins!")


    # Reset the hold condition to false on all reels
    def reset_holds(self):
        # Release all holds
        self.held = [False] * self.reels
        self.holdcount = 0

    # Caluclates the payout from the current slot positions
    def calc_payout(self):
        result = self.reel_positions
        best = 0

        for symbol in set(result):
            # Count each of the symbols in the current state
            count = result.count(symbol)
            # Check for the combination in the payout table
            payout = self.payouts.get((symbol, count), 0)
            # Find the best winning combo we have
            best = max(best, payout)

        # Update internal values
        self.currentmoney -= self.spincost
        self.lastpayout = best
        self.currentmoney += self.lastpayout
        self.totalpayout += self.lastpayout

         # Disable holds after a win
        if best > 0:
            self.reset_holds()
            self.allowholds = False
#        elif self.holdcount > self.maxholdcount:
#                self.reset_holds()
#                self.allowholds = False
        else:
            self.allowholds = True # Keep allowing holds on a non-win   
    

    def display(self):
        # Print current state
        display = []
        for i, symbol in enumerate(self.reel_positions):
            # add spaces on side of the symbol if it's not the 3 letter "BAR"
            if symbol != "BAR":
                symbol_str = f" {symbol} "
            else: 
                symbol_str = symbol
            # put braces around held symbols to indicate 'held'
            if self.held[i]:
                display.append(f"[{symbol_str}]") # held
            else:
                display.append(f" {symbol_str} ")
        print("|".join(display))


    def start_machine(self):
        # Start the slot machine
        print(f"💵🎰💵 Welcome to the Slot Machine! 💵🎰💵 €{self.spincost}.00 to spin! \n")

        while True:
            # Spin all non-held reels
            self.spin_all()
            self.display()
            self.calc_payout()
            print(f"💵 Wallet: €{self.currentmoney}.00, 💵 Payout: €{self.lastpayout}.00, 💵 Session Winnings: €{self.totalpayout}.00")

            # Ask the player if they want to hold reels
            hold_input = input(f"SPIN #: {self.spincount} | Enter reel numbers to (un)hold (1-3, comma-separated), ENTER to spin again, or q to quit:\n").strip()
            if hold_input.lower() == "q":
                print("💵🎰💵 Thanks for playing! 💵🎰💵")
                break

            if hold_input:
                # Split input by commas
                raw_values = hold_input.split(",")
                # Init an empty list for reel indices
                indices = []

                for x in raw_values:
                    x = x.strip() # Remove any leading/trailing spaces
                    if x.isdigit():
                        index = int(x) - 1 # Convert to a 0-based index (reel 1 is really reel 0)
                        if 0 <= index < 3: # 3 slot reels 0-2
                            indices.append(index) # add to the list

                # Toggle each selected reel once
                for idx in indices:
                    if 0 <= idx < 3: # Make sure index is between 0 and 2 for the 3 reels
                        self.change_hold_reel_state(idx)

            if self.currentmoney < self.spincost:
                print("You don't have enough money to play, game over!")
                break



def main():
    slot = SlotMachine()
    slot.start_machine()



if __name__ == "__main__":
    main()

