def create_matrix() -> list | None:
    while True:
        try:
            rows = int(input("Введіть кількість рядків: "))
            break
        except:
            print("Некоректні дані! Спробуйте ще.")
    while True:
        try:
            cols = int(input("Введіть кількість стовпців: "))
            break
        except:
            print("Некоректні дані! Спробуйте ще.")
    while True:
        matrix = []
        for i in range(rows):
            matrix.append([int(x) for x in input().split()])

        if len(matrix) != rows:
            print("Забагато чи замало рядків")
        for i in matrix:
            if len(i) != cols:
                print("Забагато чи замало стовпців")
        else:
            return matrix

def multiply_by_number(matrix) -> list:
    while True:
        try:
            number = int(input("Введіть число: "))
            break
        except:
            print("Неправильні дані! Спробуйте ще раз.")
    return [[num*number for num in row] for row in matrix]

def transposite(matrix) -> list:
    return [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]

def multiply_by_matrix(matrix_1, matrix_2) -> list:
    if len(matrix_1[0]) != len(matrix_2):
        return "Такі матриці не можна множити!"
    result = [[0 for i in range(len(matrix_2[0]))] for x in range(len(matrix_1))]
    for a in range(len(matrix_1)):
        for b in range(len(matrix_2[0])):
            for c in range(len(matrix_2)):
                result[a][b] += matrix_1[a][c] * matrix_2[c][b]
    return result

def add(matrix_1, matrix_2) -> list:
    return [[matrix_1[row][num]+matrix_2[row][num] for num in range(len(matrix_1[row]))] for row in range(len(matrix_1))]

def subtract(matrix_1, matrix_2) -> list:
    return [[matrix_1[row][num]-matrix_2[row][num] for num in range(len(matrix_1[row]))] for row in range(len(matrix_1))]

def main():
    while True:
        print("""
    Виберіть дію: 
    1) Додавання 2-х матриць
    2) Віднімання 2-х матриць
    3) Множення матриці на число
    4) Множення матриці на матрицю
    5) Транспонування матриці
    6) Вийти з програми
    """)
        operation = input("-> ")
        if operation in "123456":
            match operation:
                case "1":
                    result = add(create_matrix(),create_matrix())
                case "2":
                    result = subtract(create_matrix(),create_matrix())
                case "3":
                    result = multiply_by_number(create_matrix())
                case "4":
                    result = multiply_by_matrix(create_matrix(),create_matrix())
                case "5":
                    result = transposite(create_matrix())
                case "6":
                    exit()
            for i in result:
                print(i)
            break
        else:
            print("Неправильна операція! Спробуйте ще.")

while True:   
    main()