# # # # # # # # # # num_of_cups = [1, 0, 0]
# # # # # # # # # # num = int(input("from 1 to 3 \nEnter a number of cup: "))
# # # # # # # # # # from random import shuffle
# # # # # # # # # # def shuffle_cups(x):
# # # # # # # # # #     shuffle(x)
# # # # # # # # # #     return x
# # # # # # # # # # def choose (num,list,z):
# # # # # # # # # #     while z =="a":
# # # # # # # # # #         list = shuffle_cups(list)
# # # # # # # # # #
# # # # # # # # # #         if list[num - 1] == 1:
# # # # # # # # # #             z = "b"
# # # # # # # # # #             print("u win")
# # # # # # # # # #         else:
# # # # # # # # # #             print("u lose")
# # # # # # # # # # def game(answer,list):
# # # # # # # # # #     # while answer != 1 or answer != 2 or answer != 3:
# # # # # # # # # #     #     num = int(input("from 1 to 3 \nEnter a number of cup: "))
# # # # # # # # # #     z="a"
# # # # # # # # # #     shuffle_cups(list)
# # # # # # # # # #     choose(answer,list,z)
# # # # # # # # # # game(num,num_of_cups)
# # # # # # # # # # print(num_of_cups)
# # # # # # # # # # def x(*z):
# # # # # # # # # #     return sum(z)*0.05
# # # # # # # # # # print(x(5,6,5,6,8))
# # # # # # # # # # def lesser_of_two_event(a,b):
# # # # # # # # # #     if a%2==0 and b%2==0:
# # # # # # # # # #         if a<b:
# # # # # # # # # #             return a
# # # # # # # # # #         else:
# # # # # # # # # #             return b
# # # # # # # # # #     else:
# # # # # # # # # #         if a>b:
# # # # # # # # # #             return a
# # # # # # # # # #         else:
# # # # # # # # # #             return b
# # # # # # # # # # print(lesser_of_two_event(2,5))
# # # # # # # # # # a = str(input("Enter your"))
# # # # # # # # # # b = str(input("Enter"))
# # # # # # # # # # def check(a,b):
# # # # # # # # # #     if a[0]==b[0]:
# # # # # # # # # #         return True
# # # # # # # # # #     else:
# # # # # # # # # #         return False
# # # # # # # # # # print(check(a,b))
# # # # # # # # # M="macdonals"
# # # # # # # # #
# # # # # # # # # def capi(Z):
# # # # # # # # #     first=Z[0].capitalize()
# # # # # # # # #     second=Z[1:3]
# # # # # # # # #     forth=Z[4:]
# # # # # # # # #     third=Z[3].capitalize()
# # # # # # # # #     print(first+second+third+forth)
# # # # # # # # # capi(M)
# # # # # # # # #
# # # # # # # # # # print(M[0])
# # # # # # # # #
# # # # # # # # # text=input("Enter")
# # # # # # # # # def rev():
# # # # # # # # #     texr_list=text.split()
# # # # # # # # #     return texr_list[::-1]
# # # # # # # # #
# # # # # # # # # final=" ".join(rev())
# # # # # # # # # print(final)
# # # # # # # # #
# # # # # # # # num = int(input("Enter a number: \n"))
# # # # # # # # def sec(x):
# # # # # # # #     if x<150:
# # # # # # # #         res = abs(100-x)
# # # # # # # #     elif x<250:
# # # # # # # #         res = abs(200-x)
# # # # # # # #     if res<= 10:
# # # # # # # #         print(True)
# # # # # # # #     elif res>10: print(False)
# # # # # # # # sec(num)
# # # # # # #
# # # # # # # num=input("Enter a number")
# # # # # # # num_list= num.split()
# # # # # # # z= "".join(num_list)
# # # # # # # def proces():
# # # # # # #     for i in range(0,len(num_list)-1):
# # # # # # #
# # # # # # #         if num_list[i] == "3":
# # # # # # #             if num_list[i]==num_list[i+1]:
# # # # # # #                 z=1
# # # # # # #             else:z=0
# # # # # # #         else:z=0
# # # # # # #     if z==1:
# # # # # # #         print(True)
# # # # # # #     elif z==0:
# # # # # # #         print(False)
# # # # # # #
# # # # # # # proces()
# # # # # # # print(z)
# # # # # # z=input("enter your:\n")
# # # # # #
# # # # # # def zzz(z):
# # # # # #     m = ""
# # # # # #     for i in z:
# # # # # #         m+=i*3
# # # # # #     print(m)
# # # # # # zzz(z)
# # # # # def blackjack(a,b,c):
# # # # #     result=0
# # # # #     if (a+b+c) <=21:
# # # # #         result=a+b+c
# # # # #         print(result)
# # # # #     elif a+b+c> 21 and 11 in [a,b,c]:
# # # # #         result= (a+b+c)-10
# # # # #         print(result)
# # # # #     elif a+b+c>21 and 11 not in [a,b,c] : print('bust')
# # # # # blackjack(10,20,11)
# # # # num=[1,2,3,6,7,8,9,10]
# # # #
# # # # def summer_69(num):
# # # #     lsu = 0
# # # #     flag=True
# # # #     for i in range(0,len(num)):
# # # #         if num[i]!=6 and flag:
# # # #             lsu+=num[i]
# # # #         elif num[i]==6:
# # # #             flag=False
# # # #         elif num[i] ==9:
# # # #             flag=True
# # # #     print(lsu)
# # # # summer_69(num)
# # # x = input("Enter a number:\n ")
# # # def spy_game(x):
# # #     res=""
# # #     for i in x:
# # #         if i in ['0','7']:
# # #             res+=i
# # #     if "007" in res:
# # #         print(True)
# # #     else:
# # #         print(False)
# # # spy_game(x)
# # x=int(input("Enter the Num \n"))
# # def primes (x):
# #     prime_list=[]
# #     if x>2:
# #         prime_list.append(2)
# #     if x>3:
# #         prime_list.append(3)
# #         for i in range(3,x,2) :
# #             if i%3 !=0:
# #                 prime_list.append(i)
#      print(prime_list)
#      print(len(prime_list))
#  primes(x)
#  l=[1,2,3,4,5,6,7,8,9]
#  def x(i): i*2
#  print(list(map(x,l)))
# x=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x:x%2==0,x)))*****************************************************************************
# def vol (x=int(input("Enter a number: "))):
#     volume=1
#     volume=(4/3)*(22/7)*x**3
#     print(f"The volume is {volume}")
#  vol()
# def check(num,low,max):
#     if num>low and num<max:
#         print(num)
# check(5,2,7)
# def calc(x=input("Enter your sentence")):
#     UPercase = 0
#     LOwercase = 0
#     for i in x:
#         if i.isupper():
#             UPercase+=1
#         elif i.islower():
#             LOwercase+=1
#         else:
#             pass
#     print(UPercase,LOwercase)
# calc()
# def unique(x=[1,1,1,2,2,2,3,3,3,5]):
#     m=[]
#     for i in x:
#         if i not in m:
#             m.append(i)
#         else:pass
#     print(m)
# unique()
# def sun(x=[1,2,3,-4]):
#     sum=1
#     for i in x:
#         sum=int(i)*sum
#     return sum
# print(sun())
# def palindrome(x=[input('Enter a string:\n ')]):
#     z=[]
#     for i in x:
#         if i == i[::-1]:
#             z.append(i)
#         else:
#             pass
#     return z
# print(palindrome())
# names = ['ahmed', 'zanaty', 'mohamed']
# filter(lambda x: print(x), names)********************************************************************************
# inte = input("Enter a number: ")
# if inte.isdigit():
#     print(int(inte))
# else :
#     print("Invalid")
# choice_list=['0','1','2']
# def display():
#     print("Here is the current list:\n",choice_list )
# def position_choice():
#     choice = 'wrong'
#     while choice not in ['0','1','2']:
#         choice =input("enter your position choice in range(0,2)")
#         if choice.isdigit()==False:
#             print("your choice isn't in the range")
#
#     return choice
# def replace_item():
#     replace=input('enter your replacing \n')
#     return replace
# def replace(choice,replace):
#     choice_list[int(choice)]=replace
# def game():
#     con = 'y'
#     while 'y'==con:
#         display()
#         replace(position_choice(), replace_item())
#         display()
#         con = input("do you want to play again?(y/n)")
#
# game()
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.Marks = []
#         print(f'welcome {name}')
#
#     def marks(self, mark):
#         self.Marks.append(mark)
#
#     def Avg(self):
#         print(sum(self.Marks) / len(self.Marks))
#         return sum(self.Marks) / len(self.Marks)
#
#
# Ahmed = Student('Ahmed')
# Ahmed.marks(50)
# Ahmed.marks(60)
# Ahmed.marks(30)
# Ahmed.marks(40)
# Ahmed.Avg()
# class Calc:
#     def __init__(self, cor1, cor2):
#         self.cor1 = cor1
#         self.cor2 = cor2
#         print(self.cor1, self.cor2)
#
#     def dis(self):
#         print((((self.cor2[1] - self.cor1[1]) ** 2) + ((self.cor2[0] - self.cor1[0]) ** 2)) ** (1 / 2))
#
#     def slop(self):
#         print((self.cor2[1] - self.cor1[1]) / (self.cor2[0] - self.cor1[0]))
#
#
# x = Calc((1, 2), (5, 3))
# x.dis()
#
#
# class Cylinder:
#     def __init__(self, radius, height):
#         self.radius = radius
#         self.height = height
#         print(self.radius, self.height)
#
#     def volume(self):
#         return (self.radius ** 2) * self.height * 3.14
#
#     def area(self):
#         return self.radius * self.height * 2 * 3.14
#
#
# z = Cylinder(3, 2)
# print(z.volume())
# print(z.area())
# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Sorry, you don't have enough money")
#         else:
#             self.balance -= amount
#             print(f"Your operation was successful \n Your balance is {self.balance} ")
#
#     def deposite(self, amount):
#         self.balance += amount
#         print(f"Your operation was successful \n Your balance is {self.balance}")
#
#
# acc1 = Account("John", 100)
# acc1.withdraw(50)
# acc1.deposite(20)
# def tryn():
#     z = True
#     while z:
#         try:
#             x = int(input("Enter Num:\n"))
#             z = False
#             print(x)
#         except ValueError:
#             print("Invalid")
#
#
# tryn()
# dicc = {'z': 20, 'm': 6}
# dicc['z']=2
# print(dicc)

# def gen_feb(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# for x in gen_feb(10):
#     print(x)
# s='hello'
# s_it=iter(s)
# print(next(s_it))
# print(next(s_it))
# print(next(s_it))
# print(next(s_it))
# def gen_squers(n):
#     for i in range(n):
#         yield i**2
# for x in gen_squers(10):
#     print(x)
# import random
#
#
# def ran(low, high, n):
#     for i in range(n):
#         yield random.randint(low, high)
# for i in ran(1,10,12):
#     print(i)
from collections import Counter
from collections import defaultdict
from collections import namedtuple
import math
import random
import re
import time
# z=[1,1,1,2,2,2,2,3,3,6,5,5,46,4]
# Counter(z)
# print(sum(Counter(z).values()))

# d=defaultdict(lambda :0)*************************************************************************
# d['c']=1
# print(d['x'],d['c'],d[5])
# z=[1,2,3,4,5,6]
# print(list(filter(lambda x: x%2==0,z)))
# dog=namedtuple('dog',['name','bread','age'])
# sammy=dog(name='samm',bread='hasskey',age=5)
# print(sammy[0])
# print(round(5.4))
# print(random.choices(population=[1,2,3,4,5,6,7,8,9],k=8))
# print(random.sample(population=[1,2,3,4,5,6,7,8,9],k=8))
# text='my phone number is sadfd-sdfsadf sdafasdf-asdfsdfsa'
# phone_pattern=re.compile(r'[\w]+-[\w]+')
# phone=re.findall(phone_pattern,text)
# print(phone)
# s_t=time.time()
# def fun(n):
#     return (list(map(str,range(1,n+1))))
# fun(1000000000)
# print(time.time()-s_t)
import bs4
# result=requests.get('http://www.example.com')
# type(result)
# print(result.text)
# dic={a:b**2 for a,b in *zip(['m','x']*,range(2))}************************************************************************
# print(dic)
# x=[1,2,3,4,5,6,7,8,9]****************************
# x.extend([10,30])
# print(x)
# def check_input(entered, options):  # Checks whether the user entered an available number or not
#     if entered not in options:
#         return False
#     else:
#         return True
#
#
# def check_player(count):  # Checks which player is currently playing and increments the counter for players
#     if count % 2 == 0:
#         count += 1
#         return count, "Player 1"
#     else:
#         count += 1
#         return count, "Player 2"
#
#
# def check_winner(player, hand, available):  # Checks if a player has won
#     size = len(hand)
#     if size == 1 or size == 2:
#         return False
#
#     elif len(hand) > 2:
#         for i in range(size):
#             for j in range(size):
#                 if j == i:
#                     continue
#                 for k in range(size):
#                     if k == j or k == i:
#                         continue
#                     # Checks if the currently playing player has won
#                     if int(hand[i]) + int(hand[j]) + int(hand[k]) == 15:
#                         print(f'{player} has won!')
#                         return True
#                     # if no player has won and all options have been exhausted, no one wins.
#                     elif available == []:
#                         print('No one wins!')
#                         return True
#
#
# count = 0  # Used to determine which player is currently playing
# choice = None  # variable for the choice that the player makes
# options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # available options
# fin = False  # boolean to check whether the game has finished or not
# # player hands
# player1_hand = []
# player2_hand = []
#
# print('''Welcome to number scrabble!\n---------------\n
#           Rules: \n
#
#           2. For you to win, three of the numbers that you choose must add\n
#           up to be exactly 15\n
#           3. A number can only be chosen once \n
#
#           Good luck!
#
# ''')
# while True:  # loops game until player decides to exit
#     count, player = check_player(count)  # used to check which player is currently playing
#     choice = input(f"Available numbers :{options}\n{player} please choose a number: ")
#     while not check_input(choice, options):  # protects user fromm incorrect input
#
#         choice = input("Please choose a valid number: ")
#
#     options.remove(choice)  # removes selected number from the available options
#     # Adds the choice to the players' hand
#     if count % 2 == 0:
#         player1_hand.append(choice)
#         if check_winner(player, player1_hand, options):
#             fin = True
#
#     else:
#         player2_hand.append(choice)
#         if check_winner(player, player2_hand, options):
#             fin = True
#     if fin:
#         # Checks whether the players would like to play again or exit the game
#         cont = input("would you like to continue?(Y/N)").upper()
#         while cont not in ["N", "Y"]:
#             cont = input("please enter a valid choice: ").upper()
#
#         # resets all values for the nw game in case user picks to play again
#         if cont == "Y":
#             count = 0
#             choice = None
#             options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#             fin = False
#             player1_hand = []
#             player2_hand = []
#         else:  # exits the program
#             print("Goodbye!")
#             exit()
# Initialize the initial value of the sum
The_initial_value_of_sum = 0
SUM1 = 0
SUM2 = 0

while The_initial_value_of_sum < 100:
    # First player's turn
    while True:
        try:
            first_player_choice = int(input("First player, please enter a number between 1 and 10: "))
        except ValueError:
            print("please enter a valid nuber between 1 and 10")
            continue
        while first_player_choice > 10 or first_player_choice < 1:
            print("Invalid number, please enter another number between 1 and 10")
            first_player_choice = int(input("First player, please enter a number between 1 and 10: "))
            continue
        SUM1 = SUM2 + first_player_choice
        print(f'Now the sum = {SUM1}')


        if SUM1 == 100:
            print("The sum = 100")
            print("THE FIRST PLAYER HAS WON")
            break
        if SUM1 > 100:
            print("The number is over 100")
            print("game over,No one has won")
            break

        # Second player's turn


        second_player_choice = int(input("Second player, please enter a number between 1 and 10: "))


        while second_player_choice > 10 or second_player_choice < 1:
            print("Invalid number, please enter a number between 1 and 10")
            second_player_choice = int(input("Second player, please enter another number between 1 and 10: "))
            pass
        SUM2 = SUM1 + second_player_choice
        print(f'Now the sum = {SUM2}')

        if SUM2 == 100:
            print("The number is over 100")
            print("THE SECOND PLAYER HAS WON")
            break
        if SUM2 > 100:
            print("The number is over 100")
            print("game over,No one has won")
            break