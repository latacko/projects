# def any():
#     print(f"MOje var {var}")
#     print(var + 1, end='')
# var = 1
# any()
# print(var)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
    
# print(fun(fun(2)) + 1)
y = 5
def fun(x):
    # global y
    # print()
    y = x * x
    return y
    
fun(2)
print(y)

