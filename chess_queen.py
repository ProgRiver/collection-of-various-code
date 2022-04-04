
def queen_chess(lst):
    """Определяет, может ли ферзь попасть с 
       первой клетки на вторую одним ходом
    """
    x1, y1, x2, y2 = [int(i) for i in lst]

    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return "Yes"
    return "No"


coordinates = input().split()
print(queen_chess(coordinates))