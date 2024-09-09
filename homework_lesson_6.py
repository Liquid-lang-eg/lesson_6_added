
# Задание 8

# def min_max_el(matr):
#     min_el = max_el = matr[0][0]
#     for row in matr:
#         for el in row:
#             if el < min_el:
#                 min_el = el
#             if el > max_el:
#                 max_el = el
#     return min_el, max_el
#
# print(min_max_el([[1, 2], [0 ,2]]))

# Задание 9

# from random import randint

# def sum_of_matrix(M, N):
#     matrix = [[randint(0, 50) for _ in range(N)] for _ in range(M)]
#     total_sum = sum(sum(row) for row in matrix)
#     column_sums = [sum(row[col] for row in matrix) for col in range(N)]
#     percentages = {col: (col_sum / total_sum) * 100 for col, col_sum in enumerate(column_sums)}
#
#     return matrix, percentages
#
#
# N = int(input('Введите N: '))
# M = int(input('Введите M: '))
# matrix, percentages = sum_of_matrix(M, N)
#
# print(matrix)
# print("Процентные доли:", percentages)

# Задание 12

# def check_columns(matr, target):
#     for column in range(len(matr[0])):
#         for num in matr:
#             if target == num[column]:
#                 print(f'target {target} was found at column {column + 1}')
#                 break
#
#
# check_columns([[1, 2, 3], [345, 12, 1], [-12, 24, 12]], 12)


# Задание 13

# def sum_of_diagonals(matr):
#     sum_of_main = 0
#     sum_of_side = 0
#     index_1 = 0
#     index_2 = 0
#     for i in range(len(matr)):
#         sum_of_main += matr[index_1][index_2]
#         index_1 += 1
#         index_2 += 1
#     index_1 = -1
#     index_2 = 0
#
#     for i in range(len(matr)):
#         sum_of_side += matr[index_1][index_2]
#         index_1 -= 1
#         index_2 += 1
#
#     return f'сумма основной диагонали = {sum_of_main},' \
#            f' сумма побочной = {sum_of_side} '
#
#
# print(sum_of_diagonals([[1, 2, 3, 26], [345, 12, 1, 26], [-12, 24, 234, 26], [12, 456, 234, 10]]))

# Задание 14

# def make_even(matr):
#     for row in matr:
#         row.append(sum(row) % 2)
#     return matr
#
# print(make_even([[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 0, 1]]))