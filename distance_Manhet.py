
def queen_chess(lst):
    """Определяет Манхэттенское расстояние"""
    p1, p2, q1, q2 = [int(i) for i in lst]
    return abs(p1 - q1) + abs(p2 - q2)


coordinates = input().split()
print(queen_chess(coordinates))