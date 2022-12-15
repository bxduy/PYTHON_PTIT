# with open('DATA.in') as f:
# f = open('DATA.in', 'r')
# t = int(f.readline().strip())
# while t > 0:
#     t -= 1
#     n = int(f.readline().strip())
#     num = f.readline().strip()
#     if n == 2:
#         print(num)
#     else:
#         if n == 4:
#             n = 2
#         elif n == 8:
#             n = 3
#         else:
#             n = 4
#         d = len(num) % n
#         if d != 0:
#             for i in range(n - d):
#                 num = "0" + num
#
#         for i in range(0, len(num), n):
#             res = int(num[i:i + n], 2)
#             if res < 10:
#                 print(res, end="")
#             else:
#                 print(chr(res + 55), end="")
#         print()
# f.close()
f = open('DATA.in', 'a')
f.write('Hello')
f.close()