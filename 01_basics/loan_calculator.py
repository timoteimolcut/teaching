
# ── Loan payoff calculator ────────────────────────────────────────────────────
# Given a fixed monthly payment, find in which month the loan is fully paid off.

amount_owed = 28000
max_month = 130
month_pay = 428

def find_payoff_month(max_month, amount_owed):
    for i in range(max_month):
        formula1 = i * month_pay
        formula2 = (i + 1) * month_pay
        if formula1 <= amount_owed <= formula2:
            years, months = i // 12, i % 12
            remainder = formula2 - amount_owed
            print(f"Paid off in {years} years and {months} months")
            print(f"  Total paid so far : {formula1}")
            print(f"  Overshoot (change): {remainder}")
            break
        else:
            print(f"  Month {i:>3} ({i//12}y {i%12:>2}m) — paid so far: {formula1}")

find_payoff_month(max_month, amount_owed)
