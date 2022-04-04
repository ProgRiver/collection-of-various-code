
def horse_chess(lst):
    """Определяет, может ли конь попасть с 
       первой клетки на вторую одним ходом
    """
    x1, y1, x2, y2 = [int(i) for i in lst]

    if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
        return "Yes"
    return "No"


coordinates = input().split()
print(horse_chess(coordinates))