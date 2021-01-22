def calculate(days):
    payment = 200
    money = 0
    for i in range(0, days):
        money += payment
        
    if days > 14 and days <= 30:
        for i in range(14, days):
            money += 50
    if days > 30 and days <= 60:
        for i in range(30, days):
            money += 80
    if days > 60:
        for i in range(60, days):
            money += 100
            
    return money