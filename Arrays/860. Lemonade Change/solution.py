def lemonadeChange(bills) -> bool:
    bills_count = {5: 0, 10: 0, 20: 0}
    for bill in bills:
        if bill == 5:
            bills_count[bill] += 1
        elif bill == 10:
            if bills_count[5] > 0:
                bills_count[bill] += 1
                bills_count[5] -= 1
            else:
                return False
        elif bill == 20:
            if bills_count[10] > 0 and bills_count[5] > 0:
                bills_count[10] -= 1
                bills_count[5] -= 1
                bills_count[bill] += 1
            elif bills_count[5] > 2:
                bills_count[5] -= 3
                bills_count[bill] += 1
            else:
                return False
    return True
