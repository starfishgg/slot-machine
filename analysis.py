# analysis.py
from slots import SlotMachine
from settings import SLOT_PAYOUTS, FRUIT_SYMBOLS, HIGH_SYMBOLS, EXPECTED_RTP, SLOT_WEIGHTS, SLOT_SYMBOLS




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

    # For more detailed analysis (z-test, confidence intervals, etc.) we could also store every payout value in a list
    payouts = []

    for _ in range(num_spins):
        slot.spin_all()

        # Store spin results + calculate payout
        result = slot.reel_positions
        payout = slot.calc_payout()

        payouts.append(payout)
        
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
    rtp_ratio = total_payout / total_wagered
    rtp_percentage = rtp_ratio * 100
    win_rate = (wins / num_spins) * 100
    avg_payout = total_payout / num_spins

    # Calculate mean, variance, and standard deviation of payouts for more detailed analysis
    mean = rtp_ratio # sum(payouts) / num_spins


    # Calculate the variance/standard deviation of payouts
    total_squared_diff = 0
    
    for x in payouts:
        diff = x - mean
        total_squared_diff += diff * diff

    variance = total_squared_diff / num_spins
    std_dev = variance ** 0.5


    expected_rtp = EXPECTED_RTP
    expected_rtp_percentage = expected_rtp * 100

    if std_dev == 0:
        z_score = 0
        se = 0
        print("⚠️ No variance detected (all payouts identical)")
    else:
        se = std_dev / (num_spins ** 0.5)
        z_score = (mean - expected_rtp) / se

    critical_value = 1.96 # for 95% confidence interval
    ci_low = mean - critical_value * se
    ci_high = mean + critical_value * se


    # Print summary report
    print("📊📈📝 SLOT MACHINE ANALYSIS 📝📈📊")
    print(f"Spins Simulated: {num_spins:,}")
    print(f"Total Wagered: €{total_wagered:,.2f}")
    print(f"Total Paid Out: €{total_payout:,.2f}")
    print(f"RTP: {rtp_percentage:.2f}%")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Cost/Spin: €{slot.spincost:.2f}")
    print(f"Average Payout/Spin: €{avg_payout:.2f}")

    # Print total frequency breakdown
    print("\n-=TOTAL SYMBOL FREQUENCIES=-")
    print("SYMBOL \tOBSERVED \tOB.% \tEXPECTED")
    sorted_symbols = sorted(
        symbol_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    total_symbol_count = 0
    for symbol, count in sorted_symbols:
        total_symbol_count += count

    for symbol, count in sorted_symbols:
        print(f"{symbol} \t{count} \t\t{count/total_symbol_count:.2%} \t{SLOT_WEIGHTS[SLOT_SYMBOLS.index(symbol)]}%")


    print("\n-=WIN CONDITION FREQUENCIES=-")

    sorted_wins = sorted(
        win_conditions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    ev = 0

    for condition, frequency in sorted_wins:
        symbol, count = condition

        # Get payout value for this combo
        payout_per_win = slot.get_payout(symbol, count)
        # Total amount paid out by this combo overall
        total_generated = frequency * payout_per_win
        # Percentage contribution of this combo to overall RTP
        rtp_contribution = total_generated / total_wagered
        rtp_contribution_percent = rtp_contribution * 100

        probability = frequency / num_spins

        hit_rate = probability * 100
        win_share = (frequency / wins ) * 100
        print(
            f"{symbol} x{count}: "
            f"{frequency:,} wins\t| "
            f"{hit_rate:.2f}% Hit Rate\t| "
            f"{win_share:.2f}% Win Share\t| "
            f"€{total_generated:,} paid\t| "
            f"{rtp_contribution_percent:.2f}% RTP Contribution"
        )

        # Expected Value calculations
        probability = frequency / num_spins
        payout = slot.get_payout(symbol, count)
        ev += probability * payout
    
    ev -= slot.spincost        

    print("\n📊 STATISTICAL VALIDATION 📊")

    print(f"Calculated EV: {ev:.4f} per spin")
    print(f"Observed RTP: {rtp_percentage:.2f}%")
    print(f"Expected RTP: {expected_rtp_percentage:.2f}%")

    print(f"Z-Score: {z_score:.3f}")
    print(f"Standard Error: {se:.5f}")
    print(f"Standard Deviation per spin: €{std_dev:.4f}")
    
    print(f"95% Confidence Interval: [{ci_low*100:.2f}%, {ci_high*100:.2f}%]")

    print("\n📌 CONCLUSION:")
    if z_score < -critical_value:
        print(
            f"⚠️ RTP is significantly lower than expected (z = {z_score:.3f}). "
            "Model may be too strict."
        )
        
    elif z_score > critical_value:
        print(
            f"⚠️ RTP is significantly higher than expected (z = {z_score:.3f}). "
            "Model may be too generous."
        )
    else: 
        print(
            f"✅ No statistically significant deviation detected (z = {z_score:.3f}). "
            "Observed RTP is consistent with theoretical model."
        )



if __name__ == "__main__":
    simulate_spins()
