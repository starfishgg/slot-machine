# analysis.py
from slots import SlotMachine
from settings import SLOT_PAYOUTS, FRUIT_SYMBOLS, HIGH_SYMBOLS




# Run a Monte Carlo simulation of many spins to analyse machine performance
# We use this to estimate:
# - RTP (Return to Player)
# - Average payout per spin
# - Win rate
# - Symbol frequency / weighting effectiveness
def simulate_spins(num_spins=100000):

    # Create a fresh slot machien for testing
    slot = SlotMachine()

    # Running totals
    total_wagered = 0
    total_payout = 0
    wins = 0

    # Dictionary to track how often each symbol appears overall
    symbol_counts = {}

    # Track winning combinations
    win_conditions = {}

    for _ in range(num_spins):
        slot.spin_all()

        # Store spin results + calculate payout
        result = slot.reel_positions
        payout = slot.calc_payout()
        
        # Add to running totals
        total_wagered += slot.spincost
        total_payout += payout

        # Count wins
        if payout > 0:
            wins += 1

        # Track every symbol rolled for frequency analysis
        for reel in result:
            symbol_counts[reel] = symbol_counts.get(reel, 0) + 1

        # Find winning combo for this spin
        for symbol in set(result):

            # Count how many times that symbol appears
            count = result.count(symbol)

            # Record any valid 2+ or 3 matching symbols
            if slot.is_win(symbol, count):
                key = (symbol, count)

                # If this combo hasn't appeared before, add it
                if key not in win_conditions:
                    win_conditions[key] = 0

                # Increase occurrence counter
                win_conditions[key] += 1

                # Stop after recording first valid win
                break



    # Calculate statistics after all spins complete
    rtp = (total_payout / total_wagered) * 100
    win_rate = (wins / num_spins) * 100
    avg_payout = total_payout / num_spins


    # Print summary report
    print("📊📈📝 SLOT MACHINE ANALYSIS 📝📈📊")
    print(f"Spins Simulated: {num_spins:,}")
    print(f"Total Wagered: €{total_wagered:,.2f}")
    print(f"Total Paid Out: €{total_payout:,.2f}")
    print(f"RTP: {rtp:.2f}%")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Cost/Spin: €{slot.spincost:.2f}")
    print(f"Average Payout/Spin: €{avg_payout:.2f}")

    # Print total frequency breakdown
    print("\n-=TOTAL SYMBOL FREQUENCIES=-")

    sorted_symbols = sorted(
        symbol_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for symbol, count in sorted_symbols:
        print(f"{symbol}\t: {count}")

    print("\n-=WIN CONDITION FREQUENCIES=-")

    sorted_wins = sorted(
        win_conditions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for condition, frequency in sorted_wins:
        symbol, count = condition

        # Get payout value for this combo
        payout_per_win = slot.payouts.get((symbol, count), 0)
        # Total amount paid out by this combo overall
        total_generated = frequency * payout_per_win
        # Percentage contribution of this combo to overall RTP
        rtp_contribution = total_generated / total_wagered * 100
        hit_rate = (frequency / num_spins) * 100
        win_share = (frequency / wins ) * 100
        print(
            f"{symbol} x{count}: "
            f"{frequency:,} wins\t| "
            f"{hit_rate:.2f}% Hit Rate\t| "
            f"{win_share:.2f}% Win Share\t| "
            f"€{total_generated:,} paid\t| "
            f"{rtp_contribution:.2f}% RTP Contribution"
        )
    




if __name__ == "__main__":
    simulate_spins()
