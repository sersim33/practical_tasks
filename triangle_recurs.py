def triangle(num):
    if num == 1:
        return 1
    return num + triangle(num - 1)

def square(num):
    
    return triangle(num ) + triangle(num - 1)

rt = square(7)
print(rt)

