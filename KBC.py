print("Welcome to Kaun Banega Crorepati (KBC).\nTo play the game user is required to enter the serial number of the question they want to answer.\n")

userName = input("Enter your name: ")

print(userName, " Enter the serial number of the question you want to answer. For your reference there are 12 questions.\n Each question is worth a certain amount, if you select the correct answer you will be able to answer the next question in the game.\n To see the prices of the 12 Question, mind the next prompt")


    
questionNo = ["Questions no. 1", "Questions no. 2", "Questions no. 3", "Questions no. 4", "Questions no. 5", "Questions no. 6", "Questions no. 7", "Questions no. 8", "Questions no. 9", "Questions no. 10", "Questions no. 11", "Questions no. 12"]

num = 16000
limit = 50000000
prices = [num];
for i in range(100):
    num *= 2
    if num < limit:
        prices.append(num)
    
for item1, item2 in zip(questionNo, prices):
    print(f"{item1} : {item2}")


pricesOfQuestions = input("To see the prices of Questions enter the string 'Yes' to ignore enter 'No'.")

if pricesOfQuestions == "Yes" or pricesOfQuestions == 'Yes':




questions = ["What Is The Capital Of India?", 

"Who Was The First Prime Minister Of India?", 

"Which River Is Known As The Ganga Of The South?", 

"In Which Year Did India Conduct Its First Nuclear Test?", 

"Who Was The First Woman To Become The President Of India?", 

"Which Indian Scientist Won The Nobel Prize In Physics In 1930?", 

"Which Country Is Known As The Land Of The Rising Sun?", 

"Who Painted The Famous Artwork Called The Mona Lisa?", 

"What Is The Currency Of South Korea?", 

"Which Is The Largest Desert In The World?", 

"Who Was The First Woman To Travel Into Space?", 

"Which Ancient Library, Considered One Of The Greatest Of Human Civilization, Was Destroyed In A Series Of Fires In The City Of Alexandria?"]

correctAnswers = ["NEW DELHI", 

"JAWAHARLAL NEHRU", 

"GODAVARI", 

"1974", 

"PRATIBHA PATIL", 

"C. V. RAMAN", 

"JAPAN", 

"LEONARDO DA VINCI", 

"SOUTH KOREAN WON", 

"ANTARCTICA", 

"VALENTINA TERESHKOVA", 

"THE LIBRARY OF ALEXANDRIA"]

while True:
  continueOrQuit = input("To continue enter 'C'.\nTo quit enter 'Q'")
  userInpQues = int(input("Enter the serial number of question you want to answer.\nThe difficulty increases with price: "))
    
  if (continueOrQuit == "Q" or continueOrQuit == 'q'):
    print("To play restart the program")
    break
  match userInpQues:
       case 1:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1], " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
          break
       case 2:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 3:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 4:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 5:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 6:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 7:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 8:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 9:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 10:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 11:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case 12:
        print(questionNo[userInpQues - 1], " for price ", prices[userInpQues - 1], " is: ")
        print(questions[userInpQues - 1])
        answer = input("\n\n Enter your answer: ")
        answer1 = answer.upper()
        c = prices[userInpQues - 1]
        if answer1 == correctAnswers[userInpQues - 1]:
          print("Congratulations, You have won ", prices[userInpQues - 1] + c, " Rupees")
        else:
          print("You have lost your amount earned and must go without any money. \nNice playing with you.")
       case _:
        print("There is some issue with the technological aspects of the game, we will retrun shortly")
