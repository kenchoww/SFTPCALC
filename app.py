def get_score_A(days):
    if days <= 2:
        return 10
    elif days <= 4:
        return 7.5
    elif days <= 6:
        return 5
    elif days <= 8:
        return 2.5
    else:
        return 0

def get_score_B(updates_per_day):
    if updates_per_day >= 3:
        return 10
    elif updates_per_day >= 2:
        return 7.5
    elif updates_per_day >= 1:
        return 5
    elif updates_per_day >= 0.5:
        return 2.5
    else:
        return 0

def get_score_C(ratio):
    if ratio >= 5.0:
        return 10
    elif ratio >= 4.0:
        return 7.5
    elif ratio >= 2.0:
        return 5
    elif ratio >= 1.0:
        return 2.5
    else:
        return 0

def get_score_D(percent_not_delivered):
    if percent_not_delivered <= 1:
        return 10
    elif percent_not_delivered <= 2:
        return 7.5
    elif percent_not_delivered <= 5:
        return 5
    elif percent_not_delivered <= 10:
        return 2.5
    else:
        return 0

def get_score_E(percent_oos_fail):
    if percent_oos_fail <= 1:
        return 10
    elif percent_oos_fail <= 2:
        return 7.5
    elif percent_oos_fail <= 5:
        return 5
    elif percent_oos_fail <= 10:
        return 2.5
    else:
        return 0

def main():
    # Request inputs
    days = float(input("Enter the number of days vendors update their stock (A): "))
    updates_per_day = float(input("Enter the average number of stock updates per day (B): "))
    ratio = float(input("Enter the ratio of stock SFTP updates vs total assortment (C): "))
    percent_not_delivered = float(input("Enter the percentage of items not delivered (D): "))
    percent_oos_fail = float(input("Enter the percentage of OOS fail rate (E): "))
    
    # Calculate scores
    score_A = get_score_A(days)
    score_B = get_score_B(updates_per_day)
    score_C = get_score_C(ratio)
    score_D = get_score_D(percent_not_delivered)
    score_E = get_score_E(percent_oos_fail)
    
    # Calculate total score
    total_score = ((score_A + score_B + score_C + score_D + score_E) / 5) * 10
    print(f"Total SFTP Score: {total_score}")

if __name__ == "__main__":
    main()
