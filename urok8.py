# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log",
#                     filemode="w",
#                     format="we have next loading message:%(asctime)s:%(levelname)s - %message)s")
#
# # logging.debug("debug")
# # logging.info("info")
# # logging.warning("warning")
# # logging.error("error")
# # logging.critical("critical")
#
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exeption")

# assert 2 + 2 == 5, "wrong massage"

# """
# >>> 2 + 2
#
# >>> 3 - 5
#
# """
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

def adder (*args, **kwargs):
    result = 0
    for _ in args:
        result += _

        for _ in kwargs.value():
            result += _

        return result

