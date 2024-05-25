my_list = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]
iterator = iter(my_list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for  i in iterator:
#     print(i)
#
# for  i in iterator:
#     print(i)
#
# for  i in iterator:
#     print(i)

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#
#         if self.i > self.max_number:
#             raise StopIteration
#
#         return self.i
#
# count = Counter(10)
# iter(count)
#
# for  i in iterator:
#      print(i)
#
# def raise_to_the_degrees(number, max_degress):
#     result = 0
#     while True:
#         yield result
#         result = number**1
#         if result > 100**20:
#             return
#         i += 1
#
# res = raise_to_the_degrees(12,10)
# print(res)
#
# for i in res:
#      print(i)





def cheker(function):
    def cheker( *args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as ex:
            print(f"we have some problem - {ex}")
        else:
            print(f"No problem was detected.Result - {result}")

        return cheker


@cheker
def calculator(exprission):
    return eval(exprission)

calculator("2+2")


