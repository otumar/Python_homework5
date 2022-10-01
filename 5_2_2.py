# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# Игра ботом

from random import randint

player1 = input("Enter 1 player name: ")
player2 = "Bot"
quantity = int(input("Enter the number of sweets: "))

flag = randint(0, 2)  
if flag:
    print(f"{player1}, your turn")
else:
    print(f"{player2}, your turn")

def input_info(name):
    number = int(input(f"{name},  enter the number of sweets you want to take (not more than 28):  "))
    while number < 1 or number > 28:
        number = int(input(f"{name},  enter the correct number: "))
    return number


def print_info(name, sweet, counter, quantity):
    print(f"{name}, you took {sweet} sweets. Now you have {counter} sweets. There are {quantity} sweets on the table.")

counter1 = 0
counter2 = 0

while quantity > 28:
    if flag:
        sweet = input_info(player1)
        counter1 += sweet
        quantity -= sweet
        flag = False
        print_info(player1, sweet, counter1, quantity)
    else:
        sweet = randint(1, 29)
        counter2 += sweet
        quantity -= sweet
        flag = True
        print_info(player2, sweet, counter2, quantity)

if flag:
    print(f"{player1}, you are the winner! Our congratulations!")
else:
    print(f"{player2}, you are the winner! Our congratulations!")
  
