# num = [1, 2, 3]
# num2 = [4, 5, 6]
# num3 = [7, 8, 9]
# #
# print(sum(num)/len(num))


# profile = {"name": "xiaoming", "age": 27}
# ext_info = {"gender": "male"}
#
# profile += ext_info
#
# print(profile)


# def decorator(func):
#     def wrapper(*args, **kw):
#         return func()
#
#     return wrapper
#
#
# @decorator
# def function():
#     print("hello, decorator")
# my_list = [i*2 for i in range(10)]
# print(my_list)
#
# def deco():
#     name = "MING"
#     def wrapper():
#         print(name)
#     return wrapper
#
# deco()()

# def deco():
#     age = 10
#     def wrapper():
#         print(age)
#     return wrapper
#
# deco()()

# def foo():
#     print("I am a func")
#
# def bar():
#     foo="I am a string"
#     foo_dup = globals().get("foo")
#     foo_dup()
#
# bar()

news_add = (1,2,lambda a, b: a + b)
print(news_add)


def func(a, b, fun):
    s = fun(a, b)
    return s


z = func(1,2,lambda a, b: a + b)
print(z)