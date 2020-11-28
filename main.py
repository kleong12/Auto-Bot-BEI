# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import weather_forecast
from weather_forecast import forecast

from googlesearch import search
from youtube_search import YoutubeSearch

import yfinance as yf
import smtplib as bot
import imaplib as imap
import email

import time
from GoogleNews import GoogleNews
import json

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
from datetime import date
import random

today = date.today()

d1 = today.strftime("%Y-%m-%d")



def game():

    for i in range(1000):

        request = input('Auto-Bot at your service. Please state your request. ')

        if request == 'google':
            query = input('Search: ')
            print(search(query, num_results = 3))


        elif request == 'stocks':
            ticker = input('Ticker Symbol: ')
            realticker = yf.Ticker(ticker)
            print(realticker.history(period= '1m'))

        elif request == 'weather':
            place = input('City: ')
            weather = weather_forecast.forecast(place=place, time=current_time, date=d1)
            


        elif request == 'email':
            to = input('Email address: ')
            content = input('What do you want to say? ')






            address = 'autobotbei@gmail.com'
            password = 'AutoBot1'
            server = 'imap.gmail.com'



            s = bot.SMTP(host= 'smtp.gmail.com', port= 587)
            s.starttls()
            s.login(address, password)
            s.ehlo()


            s.sendmail(address, to ,content)
            {}
        elif request == 'song':
            song = input('Song name: ')
            results = YoutubeSearch(song, max_results=1).to_dict()
            dict = results[0].values()
            newdict = list(dict)

            url = newdict[7]



            print(f'https://www.youtube.com{url}')

        elif request == 'news':

            news = input('Search news: ')
            gn = GoogleNews()
            top = gn.search(news)
            newnews = gn.results()

            dict = list(newnews[0].values())
            dicttwo = list(newnews[1].values())
            dictthree = list(newnews[2].values())
            dictfour = list(newnews[3].values())
            dictfive = list(newnews[4].values())



            title1 = dict[0]
            title2 = dicttwo[0]
            title3 = dictthree[0]
            title4 = dictfour[0]
            title5 = dictfive[0]

            src1 = dict[1]
            src2 = dicttwo[1]
            src3 = dictthree[1]
            src4 = dictfour[1]
            src5 = dictfive[1]

            cap1 = dict[4]
            cap2 = dicttwo[4]
            cap3 = dictthree[4]
            cap4 = dictfour[4]
            cap5 = dictfive[4]

            url1 = dict[5]
            url2 = dicttwo[5]
            url3 = dictthree[5]
            url4 = dictfour[5]
            url5 = dictfive[5]

            print(f'Title: {title1}')
            print(f'Source: {src1}')
            print(f'Caption: {cap1}')
            print(f'Url: {url1}')

            print(f'Title: {title2}')
            print(f'Source: {src2}')
            print(f'Caption: {cap2}')
            print(f'Url: {url2}')

            print(f'Title: {title3}')
            print(f'Source: {src3}')
            print(f'Caption: {cap3}')
            print(f'Url: {url3}')

            print(f'Title: {title4}')
            print(f'Source: {src4}')
            print(f'Caption: {cap4}')
            print(f'Url: {url4}')

            print(f'Title: {title5}')
            print(f'Source: {src5}')
            print(f'Caption: {cap5}')
            print(f'Url: {url5}')








        elif request == 'math':

            def add(x, y):
                return x + y

            # This function subtracts two numbers
            def subtract(x, y):
                return x - y

            # This function multiplies two numbers
            def multiply(x, y):
                return x * y

            # This function divides two numbers
            def divide(x, y):
                return x / y



            while True:
                # Take input from the user
                choice = input("Enter choice( + / - / * / / ): ")

                # Check if choice is one of the four options
                if choice in ('+', '-', '*', '/'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '+':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '-':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '*':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '/':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    break
                else:
                    print("Invalid Input")

        elif request == 'game':

            type = input('Which game? Press 1 for tic-tac-toe, press 2 for rock-paper-scissors ')

            if type == '1':
                unused_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                theBoard = {'7': ' ', '8': ' ', '9': ' ',
                            '4': ' ', '5': ' ', '6': ' ',
                            '1': ' ', '2': ' ', '3': ' '}

                board_keys = []

                for key in theBoard:
                    board_keys.append(key)

                ''' We will have to print the updated board after every move in the game and 
                    thus we will make a function in which we'll define the printBoard function
                    so that we can easily print the board everytime by calling this function. '''

                def printBoard(board):
                    print(board['7'] + '|' + board['8'] + '|' + board['9'])
                    print('-+-+-')
                    print(board['4'] + '|' + board['5'] + '|' + board['6'])
                    print('-+-+-')
                    print(board['1'] + '|' + board['2'] + '|' + board['3'])

                # Now we'll write the main function which has all the gameplay functionality.
                def tictactoe():

                    turn = 'X'
                    count = 0

                    for i in range(10):
                        printBoard(theBoard)
                        print("It's your turn," + turn + ".Move to which place?")

                        if turn == 'O':
                            choice = random.randint(1,9)
                            choice = unused_keys[choice]



                            if theBoard[f'{choice}'] == ' ':
                                theBoard[choice] = turn
                                unused_keys.remove(choice)
                                count += 1






                        elif turn == 'X':
                            move = input()

                            if theBoard[move] == ' ':
                                theBoard[move] = turn
                                unused_keys.remove(move)
                                count += 1
                            else:
                                print("That place is already filled.\nMove to which place?")
                                continue

                        # Now we will check if player X or O has won,for every move after 5 moves.
                        if count >= 5:
                            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break
                            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                                printBoard(theBoard)
                                print("\nGame Over.\n")
                                print(" **** " + turn + " won. ****")
                                break

                                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
                        if count == 9:
                            print("\nGame Over.\n")
                            print("It's a Tie!!")

                        # Now we have to change the player after every move.
                        if turn == 'X':
                            turn = 'O'
                        else:
                            turn = 'X'

                tictactoe()




            elif type == '2':
                print("Winning Rules of the Rock paper scissor game as follows: \n"
                  + "Rock vs paper->paper wins \n"
                  + "Rock vs scissor->Rock wins \n"
                  + "paper vs scissor->scissor wins \n")


                print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")


                choice = int(input("User turn: "))

                # OR is the short-circuit operator
                # if any one of the condition is true
                # then it return True value

                # looping until user enter invalid input
                while choice > 3 or choice < 1:
                    choice = int(input("enter valid input: "))

                    # initialize value of choice_name variable
                # corresponding to the choice value
                if choice == 1:
                    choice_name = 'Rock'
                elif choice == 2:
                    choice_name = 'paper'
                else:
                    choice_name = 'scissor'

                # print user choice
                print("user choice is: " + choice_name)
                print("\nNow its computer turn.......")

                # Computer chooses randomly any number
                # among 1 , 2 and 3. Using randint method
                # of random module
                comp_choice = random.randint(1, 3)

                # looping until comp_choice value
                # is equal to the choice value
                while comp_choice == choice:
                    comp_choice = random.randint(1, 3)

                    # initialize value of comp_choice_name
                # variable corresponding to the choice value
                if comp_choice == 1:
                    comp_choice_name = 'Rock'
                elif comp_choice == 2:
                    comp_choice_name = 'paper'
                else:
                    comp_choice_name = 'scissor'

                print("Computer choice is: " + comp_choice_name)

                print(choice_name + " V/s " + comp_choice_name)

                # condition for winning
                if ((choice == 1 and comp_choice == 2) or
                            (choice == 2 and comp_choice == 1)):
                    print("paper wins => ", end="")
                    result = "paper"

                elif ((choice == 1 and comp_choice == 3) or
                      (choice == 3 and comp_choice == 1)):
                    print("Rock wins =>", end="")
                    result = "Rock"
                else:
                    print("scissor wins =>", end="")
                    result = "scissor"

                # Printing either user or computer wins
                if result == choice_name:
                    print("<== User wins ==>")
                else:
                    print("<== Computer wins ==>")


'''
mail = imap.IMAP4_SSL(server)
mail.login(address, password)

mail.select('inbox')

status, data = mail.search(None, 'ALL')

ids = []
for block in data:
    ids += block.split()
for i in ids:
    status, data = mail.fetch(i, '(RFC822)')

    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            mail_from = message['from']
            mail_subject = message['subject']

            if message.is_multipart():
                mail_content = ''
                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                mail_content = message.get_payload()


print(mail_from)
s.quit()

'''
game()