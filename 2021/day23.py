# fmt: off
A, B, C, D = 1, 10, 100, 1000
# Did by eye! placed 385!
"""
#############
#...........#
###D#C#A#B###
  #B#C#D#A#
  #########
"""
part_1 = [(A,6),(B,6),(A,3),(D,6),(C,5),(C,5),(B,3),(D,8),(B,5),(A,3),(A,8)]
print(f"Part 1: {sum(e * n for e, n in part_1)}") # 15160
"""
#############
#...........#
###D#C#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #B#C#D#A#
  #########
"""
part_2 = [
    (A,7),(C,7),(C,7),(B,3),(A,8),(B,4),(C,5),(B,5),(B,6),
    (B,7),(D,5),(C,7),(C,7),(A,4),(C,7),(A,5),(D,7),(C,4),
    (D,10),(D,10),(D,10),(B,7),(A,11),(A,11),(A,3),(A,3),
]
print(f"Part 2: {sum(e * n for e, n in part_2)}") # 46772