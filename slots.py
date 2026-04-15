# slots.py
# implementation of SlotMachine class

import random # we can use previously implemented improved random number generator later
from settings import SLOT_SYMBOLS, SLOT_WEIGHTS, SLOT_PAYOUTS, STARTING_CASH, SPIN_COST, SLOT_WHEELS, HIGH_SYMBOLS, FRUIT_SYMBOLS


class SlotMachine:
    def __init__(self):
        # Symbols and weghts
        self.symbols = SLOT_SYMBOLS
        self.weights = SLOT_WEIGHTS
        self.payouts = SLOT_PAYOUTS
        self.reelcount = SLOT_WHEELS
        self.spincost = SPIN_COST
        self.startingmoney = STARTING_CASH
        self.currentmoney = STARTING_CASH


        self.spincount = 0
        self.lastpayout = 0
        self.lastwinsymbol = ""
        self.lastwinsymbolcount = 0
        self.totalpayout = 0

        self.lastwaswin = False
        self.lastwasbigwin = False
        self.holdsallowed = True
        self.holdcount = 0
        self.maxholdcount = 3 # Don't allow holding more than 1-2 times in a row



        # Track the current state of each reel
        self.reel_positions = [None] * self.reelcount

        # Track held reels (False = spin, True = hold)
        self.held = [False] * self.reelcount



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
        # Spin reels
        for i in range(self.reelcount):
            self.spin_reel(i)

        self.spincount += 1
        



    # Checks if the specified reel is in a [HOLD] state (returns true/false)
    def is_reel_held(self, index):
        return self.held[index]
    


    # Checks if any of the reels are in a [HOLD] state (returns true/false)
    def any_reels_held(self):
        return any(self.held)



    # called when hold states are received in get_input
    def set_hold(self, index, value=True):
        # Prevent holding if not allowed
        if self.holdsallowed:
            # flip hold state
            if 0 <= index < self.reelcount:
                self.held[index] = not self.held[index]



    # Allow holds
    def enable_holds(self):
        self.holdsallowed = True
        #print("🔓 Holds are unlocked!")



  # Disable holds
    def disable_holds(self):
        self.holdsallowed = False
        self.reset_holds()
        #print("🔒 Holds are locked!")


    def reset_holds(self):
        self.holdcount = 0
        for index in range(self.reelcount):
            self.held[index] = False




    def is_win(self, symbol, count):
        if symbol in HIGH_SYMBOLS:
            return count == 3
        elif symbol in FRUIT_SYMBOLS:
            return count >= 2



    def get_payout(self, symbol, count):
        return self.payouts.get((symbol, count), 0)


    
    # LOTS OF WORK TO DO HERE, MOVE ALL HOLD CHECK LOGIC HERE PROBABLY
    def apply_hold_states(self):
        
        # Unold reels and diasable holds after hold counter limit hit
        if self.holdsallowed:
            # print("🔓 Holds are allowed this round!")
            if self.any_reels_held():
                # print("🔒 Reels are beind held!")
                if self.holdcount < self.maxholdcount:
                    self.holdcount += 1
                    remaining_holds = self.maxholdcount - self.holdcount
                    print(f"🔒 Holds remaining: {remaining_holds}/{self.maxholdcount}")
                else:
                    print("🚫 Hold limit reached — holds disabled until reset")
                    self.disable_holds()
        else:
                self.holdcount = 0
                self.enable_holds()
                print("🔓 Holds are allowed this round!")
        #print("DEBUG: PRE-SPIN LOGIC")
        #print(f"DEBUG: Held Reels State: R0:{self.is_reel_held(0)}, R1:{self.is_reel_held(1)}, R2:{self.is_reel_held(2)}")
        #print(f"DEBUG: Hold Allowed State: {self.holdsallowed}")
        #print(f"DEBUG: Any Reels Held State: {self.any_reels_held()}")
        #print(f"DEBUG: Hold Count State: {self.holdcount}")
        #print(f"DEBUG: Last Win State: {self.lastwaswin}")
        #print(f"DEBUG: Last Big State: {self.lastwasbigwin}")



    def cleanup_hold_states(self):
        
        if self.lastwasbigwin:
            self.disable_holds()
            self.holdcount = 0
            self.lastwasbigwin = False
        else:
            self.enable_holds()

        if self.lastwaswin:
            self.lastwaswin = False      


        #print("DEBUG: POST-SPIN LOGIC")
        #print(f"DEBUG: Held Reels State: R0:{self.is_reel_held(0)}, R1:{self.is_reel_held(1)}, R2:{self.is_reel_held(2)}")
        #print(f"DEBUG: Hold Allowed State: {self.holdsallowed}")
        #print(f"DEBUG: Any Reels Held State: {self.any_reels_held()}")
        #print(f"DEBUG: Hold Count State: {self.holdcount}")
        #print(f"DEBUG: Last Win State: {self.lastwaswin}")
        #print(f"DEBUG: Last Big State: {self.lastwasbigwin}")

    

    # Caluclates the payout from the current slot positions
    def calc_payout(self):
        result = self.reel_positions
        best_payout = 0

        for symbol in set(result):
            # Count each of the symbols in the current state
            count = result.count(symbol)
            # Check for the combination in the payout table
            payout = self.get_payout(symbol, count)
            # Find the best winning combo we have
            best_payout = max(best_payout, payout)

            if self.is_win(symbol, count):
                # print(f"WIN: {symbol} x{count} - €{best_payout:.2f}")
                self.lastwaswin = True
                if count == 3:
                    self.lastwasbigwin = True
                    self.lastwinsymbol = symbol
                    self.lastwinsymbolcount = count
                elif count >= 2:
                    self.lastwinsymbol = symbol
                    self.lastwinsymbolcount = count
                else:
                    self.lastwinsymbol = ""
                    self.lastwinsymbolcount = 0


                
        # Update internal values
        self.currentmoney -= self.spincost
        self.lastpayout = best_payout

        self.currentmoney += self.lastpayout
        self.totalpayout += self.lastpayout

        return self.lastpayout
    


    def display(self):
        print(f"🎰 You just span the reels! -€{self.spincost:.2f}")
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
        if self.is_win(self.lastwinsymbol, self.lastwinsymbolcount):
            print(f"💵💵💵 WIN: {self.lastwinsymbol} x{self.lastwinsymbolcount} - €{self.lastpayout:.2f}")
        print(f"💵 Wallet: €{self.currentmoney:.2f}, , 💵 Session Winnings: €{self.totalpayout:.2f}")



    def get_input(self):
        # Ask the player if they want to hold reels
        hold_input = input(f"SPIN #: {self.spincount} | Enter reel numbers to (un)hold (1-3, comma-separated), ENTER to spin again, or q to quit:\n").strip()
        if hold_input.lower() == "q":
            print("👋🎰👋 Thanks for playing! 👋🎰👋")
            return False

        # Pressing [Enter] isn't a null state, it's an emptry string
        if hold_input == "":
            pass
        else:
            # Split input by commas
            raw_values = hold_input.split(",")
            new_holds = set()

            for x in raw_values:
                x = x.strip() # Remove any leading/trailing spaces
                if x.isdigit():
                    index = int(x) - 1 # Convert to a 0-based index (reel 1 is really reel 0)
                    if 0 <= index < self.reelcount : # 3 slot reels 0-2
                        new_holds.add(index)

            # Set new hold states
            for idx in new_holds:
                self.set_hold(idx, True)
        return True



    def start_machine(self):
        # Start the slot machine
        print(f"💵🎰💵 Welcome to the Slot Machine! 💵🎰💵 €{self.spincost}.00 to spin! \n")
        keepPlaying = True
        while keepPlaying:
            # Spin all non-held reels
            self.apply_hold_states()
            self.spin_all()
            self.calc_payout()
            self.display()
            self.cleanup_hold_states()
            keepPlaying = self.get_input()

            if self.currentmoney < self.spincost:
                print("You don't have enough money to play, game over!")
                break



def main():
    slot = SlotMachine()
    slot.start_machine()



if __name__ == "__main__":
    main()

