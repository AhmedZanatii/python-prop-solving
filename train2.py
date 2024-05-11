# prop1
# num1= int(input('Enter your first num: '))
# num2= int(input('Enter your first num: '))
# if ((num1 + num2)%2 == 0 ):
#     print('this sum is even')
# else: print('this sum is odd')
# prop2
# num = input("Enter the numbers:\n")
# sum = 0
# for i in num:
#     sum += int(i)
# print(f"The sum of numbers is : {sum}")
# prop3
# def power(low, high):
#     while low <= high:
#         print(low ** 2)
#         low += 1
# power(1,4)
# prop4 = prop2
# prop5
# z = input("Enter you sentence: \n")  ***********************************
# x = z.replace(" ", '')**************************************************
# n = 1
# for i in z:
#     while i == 'r':
#         print(f'r =={n}')
#         i = "f"
#     n += 1
# prop6
# the_word =input("Enter you sentence: \n")
# the_new_sentence =the_word.replace('B','C')
# print(the_new_sentence)
# prop7
# num = int(input("Enter the num:\n"))
# fact = 1
# while num != 0:
#     fact *= num
#      = num - 1
# print(fact)
# prop8
# seq = [0, 1]
#
#
# def Fibo_seq(limit):
#     while len(seq) != limit:
#         last_item = seq[-1] + seq[-2]
#         seq.append(last_item)
#     print(seq)
#
#
# Fibo_seq(int(input("Enter the limit of the Fibonacci:\n")))
# print(seq[-1])
# prop9
# base = int(input("Enter the base: \n"))
# power = int(input("Enter the power: \n"))
#
#
# def powern(base, power):
#     pow = base ** power
#
#     print(pow)
#
#
# powern(base, power)
# prop10
# num1 = int(input("Enter number1 :"))
# num2 = int(input("Enter number2 :"))
#
#
# def arranage(num1, num2):
#     if num1 > num2:
#         print(num2, ',', num1)
#     elif num1 < num2:
#         print(num1 , ',' , num2)
#     else:
#         print("Exit")
#
#
# arranage(num1, num2)
# prop11
# num_of_people = int(input("Enter the number of people: "))
# num_of_apples = int(input("Enter the number of apple: "))
# def fair_distr(num_of_people, num_of_apples):
#     print(num_of_apples%num_of_people)
# fair_distr(num_of_people, num_of_apples)
# prop12
# num = int(input("Enter a number: "))
# time = []
# def change(x):
#     while x!=0:
#         t = x % 60
#         x = (x-t) / 60
#         time.append(t)
#         print(t,x)
# change(num)
# print(int(time[-1]),':',int(time[-2]),':',':',int(time[-3]))
# # prop13
# num=input("Enter the num :\n")
# m=[]
# for i in num:
#     if i in ["a", 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'f']:
#         m.append('h')
#         pass
#     elif i in ['9', '8']:
#         m.append('d')
#         pass
#     elif i in ["7", '6', '5', '4', '3', '2']:
#         m.append('o')
#     else:
#         m.append('b')
# if 'h' in m:
#     print('num is hexa')
#     pass
# elif 'd' in m:
#     print('num is decimal')
#     pass
# elif 'o' in m:
#     print('num is octal')
# else: print('num is binary')
# prop14
# bin=input("Enter the")
# st_com=''
# for i in bin:
#     if i=='0':
#         st_com+='1'
#     else: st_com+='0'
# print(st_com)
# prop15
# bin = input("Enter the")[::-1]
# nd_com = ''
# bool = 0
# for i in bin:
#     if bool == 0:
#         if i == '0':
#             nd_com += "0"
#         elif i == '1':
#             nd_com += '1'
#             bool = 1
#     elif bool == 1:
#         if i == '0':
#             nd_com += '1'
#         else:
#             nd_com += '0'
# print(nd_com[::-1])
# a=int(input("Enter"))
# b=int(input("Enter"))
# for i in range(min(a,b),0,-1):
#     if b%i ==0 and a%i ==0:
#         print(i)
#         break
# bin = input("Enter the")[::-1]

# def sec_com(bin):
#     nd_com = ''
#     bool = 0
#     for i in bin:
#         if bool == 0:
#             if i == '0':
#                 nd_com += "0"
#             elif i == '1':
#                 nd_com += '1'
#                 bool = 1
#         elif bool == 1:
#             if i == '0':
#                 nd_com += '1'
#             else:
#                 nd_com += '0'
#     return nd_com[::-1]
#
# def supp(num1,num2):
#     nd_comp = sec_com(num2)
#     sum=''
#     carry=0
#
#     for i in range(len(nd_comp)-1,-1,-1):
#         result=int(num1[i])+int(num2[i])+carry
#         if result in [0,1]:
#             sum=str(result)+sum
#         elif result == 2:
#             sum='0'+sum
#             carry=1
#         elif result == 3:
#             sum = '1'+sum
#             carry=1
#     print(sum)
#
# supp('001001','000100')
# def supp(num1,num2):
#     num1 = num1
#     num2=sec_com(num2)

# def bin_to(bin,base):
#     sum=0
#     for i in range(0,len(bin),1):
#         sum+=int(bin[len(bin)-i-1])*(base**i)
#     print (sum)
# bin_to('10101',2)
# prop20
# def sss (min=int(input('write the min num:')),max=int(input('write the max num:')),type=input('write the type ')):
#         sum=0
#         if type== 'e':
#             for j in range(min,max+1):
#                 if j%2==0:
#                     sum=sum+j
#                 else:pass
#         if type == 'o':
#             for j in range(min, max + 1):
#                 if j % 2 == 1:
#                     sum = sum + j
#                 else:pass
#
#         print(sum)
#
#
# sss()
# prop21
# def sss (min=int(input('write the min num:')),max=int(input('write the max num:')),type=int(input('write the type '))):
#     sum=0
#     for j in range(min, max + 1):
#         if j % type == 0:
#             sum = sum + j
#         else:
#             pass
#     print(sum)
# sss()
