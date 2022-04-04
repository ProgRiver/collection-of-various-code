
def elephant_chess_piece(lst):
    """Определяет, может ли слон попасть с 
       первой клетки на вторую одним ходом
    """
    x1, y1, x2, y2 = [int(i) for i in lst]
    if (x1 - x2)**2 == (y1 - y2)**2:
        return "Yes"
    return "No"

coordinates = input().split()
print(elephant_chess_piece(coordinates))