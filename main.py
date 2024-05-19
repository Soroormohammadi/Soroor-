<<<<<<< HEAD
# def check_view(list_of_height):
#     blocked_numbers = []
#     for index0 in range(len(list_of_height)-1, 0, -1):
#         for index in range(len(list_of_height[index0])-1, -1, -1):
#             if list_of_height[index0][index] < list_of_height[index0-1][index]:
#                 blocked_numbers.append((index0-1, index))
#     return blocked_numbers
#
#
# lst0 = [[1, 2, 3, 2, 1, 1],
#         [2, 4, 4, 3, 2, 2],
#         [7, 5, 5, 10, 6, 4],
#         [6, 6, 7, 6, 5, 5]]
# print(check_view(lst0))
#
# ------------------------------------------------------
#
# def freed_prisoners(cells):
#     freed_prisoner = 0
#     if cells[0] == 0:
#         return 0
#     for index0 in range(len(cells)):
#         if cells[index0] == 1:
#             freed_prisoner += 1
#             for index in range(len(cells)):
#                 if cells[index] == 0:
#                     cells[index] = 1
#                 else:
#                     cells[index] = 0
#     return freed_prisoner
#
#
# print(freed_prisoners([0, 1, 1, 1]))
#
# -----------------------------------------------------------
#
# def find_degrees(time):
#     h = time[0:2]
#     m = time[3:5]
#     if h == 12:
#         h = 00
#     print(h, m)
#     d = (float(h)*30) - (float(m)*5.5)
#     if d < 0:
#         d = -d
#     if d > 180:
#         d = 360 - d
#     return d
#
#
# print(find_degrees("12:33"))
#
# ----------------------------------------------------
#
# def sorted_list(list_of_items):
#     sorted_lst = []
#     for index in range(len(list_of_items)):
#         x = 0
#         for index_1 in range(len(sorted_lst)):
#             if list_of_items[index] in sorted_lst[index_1]:
#                 sorted_lst[index_1].append(list_of_items[index])
#                 x += 1
#         if x == 0:
#             sorted_lst.append([list_of_items[index]])
#     return sorted_lst
#
#
# print(sorted_list(["b", "a", "b", "a", "c"]))
#
# ------------------------------------------------------------------------
#
# def simplified_fraction(x, y):
#     n1 = x
#     n2 = y
#     if x > y:
#         n = y
#     if x < y:
#         n = x
#     if x == y:
#         n = x
#         return x / y
#
#     for index in range(n, 1, -1):
#         if x % index == 0 and y % index == 0:
#             n1 = x / index
#             n2 = y / index
#             if n1 > n2:
#                 n = int(n2)
#             if n1 < n2:
#                 n = int(n1)
#             i = 1
#             break
#     if n2 == 1:
#         return int(n1)
#     if n2 == 0:
#         return 0
#     return f"{int(n1)}/{int(n2)}"
#
#
# print(simplified_fraction(400, 100))
#
# ---------------------------------------------------
#
# def bingo_check(num_list):
#     num_found = []
#     for index_0 in range(len(num_list)):
#         for index_1 in range(len(num_list[index_0])):
#             if num_list[index_0][index_1] == "x":
#                 num_found.append((index_0, index_1))
#
#     b = 0
#
#     for index_2 in range(len(num_found)):
#         x = 0
#         y = 0
#         z_0 = 0
#         z_1 = 0
#         for index_3 in range(len(num_found)):
#             if num_found[index_3][0] == index_2:
#                 x += 1
#             if num_found[index_3][1] == index_2:
#                 y += 1
#             if num_found[index_3][0] == num_found[index_3][1]:
#                 z_0 += 1
#             if num_found[index_3] in [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]:
#                 z_1 += 1
#         if x > 4 or y > 4 or z_1 > 4 or z_1 > 4:
#             b = 1
#             break
#
#     if b == 1:
#         return True
#     else:
#         return False
#
#
# print(bingo_check([
#   [45, "x", 31, 74, "x"],
#   [64, 33, 47, "x", 90],
#   [37, "x", "x", 83, 54],
#   [67, "x", 98, "x", 44],
#   ["x", "x", 24, 30, 52]
# ]))
