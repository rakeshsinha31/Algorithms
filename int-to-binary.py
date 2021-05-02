def int_to_binary(num):
    bin = []
    while num > 0:
        rim = num % 2
        bin.append(rim)
        num = num//2
    return "".join([str(i) for i in bin][::-1])


print(int_to_binary(242))
print(int_to_binary(10))
print(int_to_binary(657))
print(int_to_binary(16561))
