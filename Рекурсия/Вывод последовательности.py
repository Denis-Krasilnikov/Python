# Функция, выводящая последовательность от 1 до n на экран

def print_seq(n):
    if n == 0:
        return
    print_seq(n - 1)
    print(n, end=' ')


print_seq(10)