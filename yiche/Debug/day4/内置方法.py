# __author__ = "Alex Li"
#




# print(abs(-1))    # 返回数字的绝对值
# print(all(['ds90', 0]))     # 检查可迭代对象是否为真，是则返回True，否则返回False, 非0均为真
# print(any([1, 0]))     # 检查可迭代对象是否为空，是则返回False,否则返回True
# print(ascii([1, '王']))  # 返回对象的ascii码格式，字符串
# print(bin(12))      # 返回数字的二进制形式
# print(bool())  # 返回对象的布尔类型0、以及空对象均为False
# a = bytes('abc', encoding='utf-8')    # 转换为bytes格式
# print(bytearray())
# print(callable(abs))   # 检查对象是否可以调用（方法、函数），是则返回True,否则返回False
# print(chr(98))      # 返回字符的ascii码对照表表现字符
# print(ord('b'))     # 返回ascii码字符的的对照字符
# code = 'for i in range(10): print(i)'
# c = compile(code, '', 'exec')     #没卵用
# print(complex(1))    # 将数字转换为负数
# print(dir('1'))     # 查看对象可用方法
# print(divmod(5, 3))     # 传入除数和被除数，通过元组返回两个数字的除数和余数
# print(eval("{'a':1}"))    # 去掉引号，字符串可转list、dict、tuple

# a = '''for i in range(10):
#     print(i)'''
# exec(a)      # 可以执行储存在字符串或文件中的Python语句

# ca = lambda n: print(n)     # 匿名函数,只能完成简单的逻辑，三元环表达式等 可结合filter使用
# ca(5)

# f = filter(lambda n: n > 5, range(10))      # 用于过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成新列表,过滤器
# for i in f:
#     print(i)

# m = map(lambda n: n > 5, range(10))     # 创建一个迭代器，使用每个可迭代对象的参数计算函数。当最短的可迭代对象耗尽时停止。
# for i in m:
#     print(i)

# a = frozenset([1, 2, 3])      # 冻结，使对象变为不可变

# ab = '1'
# print(globals())    # 返回包含当前作用域全局变量的字典。尽量避免在代码中使用globals()函数，因为它可能会导致代码的可读性和可维护性降低。
# print(locals())     # 返回一个包含当前作用域局部变量的字典。

# print(hash('alex'))   # 返回对象的哈希值
# print(help()
# hasattr()
# print(hex(11))       # 返回数字的十六进制

# class Man:
#     def __init__(self):
#         print('hi')
#
#
# m = Man()
# print(isinstance(m, Man))  # 返回对象是类的实例还是类的子类的实例。是则返回True，否则返回False


# iter()
# #print( all([1,-5,3]) )
# #print( any([]) )
# # a= ascii([1,2,"开外挂开外挂"])
# # print(type(a),[a])
# # a = bytes("abcde",encoding="utf-8")
# # b = bytearray("abcde",encoding="utf-8")
# # print( b[1] )
# # b[1]= 50
# # print(b)
#
#
# #print(a.capitalize(),a)
# # def sayhi():pass
# # print( callable(sayhi) )
#
# code = '''
# def fib(max): #10
#     n, a, b = 0, 0, 1
#     while n < max: #n<10
#         #print(b)
#         yield b
#         a, b = b, a + b
#         #a = b     a =1, b=2, a=b , a=2,
#         # b = a +b b = 2+2 = 4
#         n = n + 1
#     return '---done---'
#
# #f= fib(10)
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
#
# '''
#
# #py_obj = compile(code,"err.log","exec")
# #exec(py_obj)
#
# #exec(code)
#
#
# # def sayhi(n):
# #     print(n)
# #     for i in range(n):
# #         print(i)
# # sayhi(3)
# #
# # #(lambda n:print(n))(5)
# # calc = lambda n:3 if n<4 else n
# # print(calc(2))
#
# #res = filter(lambda n:n>5,range(10))
# # res = map(lambda n:n*2,range(10))
# # res = [ lambda i:i*2 for i in range(10)]
# # import functools
# # res = functools.reduce( lambda x,y:x*y,range(1,10 ))
# # print(res )
#
# a = frozenset([1,4,333,212,33,33,12,4])
# #print(globals())
#
# def test():
#     local_var =333
#     print(locals())
#     print(globals())
# test()
# print(globals())
# print(globals().get('local_var'))


# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
#
# #print(  sorted(a.items()) )
# print(  sorted(a.items(),key=lambda x:x[1]) )
# print(a )

# a = [1,2,3,4,5,6]
# b = ['a','b','c','d']
#
# for i in zip(a,b):
#     print(i)

#import 'decorator'
__import__('decorator')
