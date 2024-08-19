
def sum_and_print(n):
    if n == 1:
        print(1, end=' ')
        return 1
    else:
        result = n + sum_and_print(n-1)
        print(f'+ {n}', end=' ')
        return result

n = 5
res = sum_and_print(n)
print(f'= {res}')





