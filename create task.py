import time 
import turtle as trtl

#Had to add playsound from a download on the offical pyytho website 
from playsound import playsound



wn = trtl.Screen()
wn.setup(width=800, height=600)
trtl.hideturtle()
trtl.penup()
trtl.goto(-225,175)
trtl.write("What is your bi-weekly income in January?")
print("What is your bi-weekly income in January?")
Janincome = int(input("->"))
monthly_income = Janincome * 2
if Janincome >= 5000:
    wn.clear()
    trtl.hideturtle()
    trtl.penup()
    trtl.goto(-225,250) 
    trtl.write("Why do you need financial advice if you make so much money")
    print("Why do you need financial advice if you make so much money")
    wn.bgpic("walter.gif")
    wn.update()
    playsound("money.mp3")
    time.sleep(3)
elif monthly_income < 2000 :
    wn.clear()
    trtl.hideturtle()
    trtl.penup()
    trtl.goto(-200,175) 
    trtl.write("You are broke how are you even alive in this economy")
    print( "You are broke how are you even alive in this economy")
    wn.bgpic("hobo.gif")
    wn.update()
    playsound("sponge.mp3")
else:
    trtl.goto(-200,165)
    trtl.write("Your monthly income will be close to " + str(monthly_income) + " dollars")
    print("Your monthly income will be close to ", monthly_income, " dollars")
    #list so that you can find the actual amount you should send
    deductions = [0.35, 0.10, 0.15, 0.15, 0.20, 0.05]
    'rent , food , utilities, car, savings, entertainment'
    rent = monthly_income * deductions[0]
    print(rent, "dollars should be going to rent")
    food = monthly_income * deductions[1]
    print(food, "dollars should be going to food")
    utilities = monthly_income * deductions[2]
    print(utilities, "dollars should be going to utilities")
    car = monthly_income * deductions[3]
    print(car, "dollars should be going to car")
    savings = monthly_income * deductions[4]
    print(savings, "dollars should be going to savings")
    entertainment = monthly_income * deductions[5]
    print(entertainment, "dollars should be going to entertainment")
#   writing in the output
    time.sleep(2)
    trtl.goto(-200,155)
    trtl.write(str(rent)+ "dollars should be going to rent")
    trtl.goto(-200,145)
    trtl.write(str(food)+ "dollars should be going to food")
    trtl.goto(-200,135)
    trtl.write(str(utilities)+ "dollars should be going to utilites")
    trtl.goto(-200,125)
    trtl.write(str(car)+ "dollars should be going to car")
    trtl.goto(-200,115)
    trtl.write(str(savings)+ "dollars should be going to savings")
    trtl.goto(-200,105)
    trtl.write(str(entertainment)+ "dollars should be going to entertainment")
    

    trtl.goto(-200,95)
    trtl.write("What is your bi-weekly in February?")
    print("What is your bi-weekly in February?")
    Febincome = int(input("->"))
    if Febincome > Janincome:
        trtl.goto(-200,85)
        trtl.write("You made a profit keep it up and you will be a millionaire")
        print("You made a profit keep it up and you will be a millionaire")
        time.sleep(2)
        trtl.goto(-200,75)
        trtl.write("Their are always ways to increase your wealth even further")
        print("Their are always ways to increase your wealth even further")
        time.sleep(2)
        wn.clear()
        wn.bgpic("money.gif")
        trtl.penup()
        trtl.goto(-200,-190)
        trtl.write("You can invest your money in stocks, bonds, real estate, and even cars")
        print( "You can invest your money in stocks, bonds, real estate, and even cars")
        wn.update()
        playsound("cash.mp3")
    elif Febincome == Janincome:
        trtl.goto(-200,85)
        trtl.write("You broke even not good or bad ")
        print("You broke even not good or bad ")
        time.sleep(2)
        trtl.goto(-200,75)
        trtl.write("Here are some things that can help improve your finances")
        print("Here are some things that can help improve your finances ")
    else:
        trtl.goto(-200,85)
        trtl.write(" You made a loss you should be more careful")
        print("You made a loss you should be more careful")
        time.sleep(2)
        trtl.goto(-200,75)
        trtl.write("Here are some things that can help improve your finances ")
        print("Here are some things that can help improve your finances ")
    if Febincome <= Janincome:
        time.sleep(2)
        trtl.goto(-200,65)
        trtl.write("You should consider job hoping ")
        print("You should consider job hoping")
        time.sleep(2)
        trtl.goto(-200,55)
        trtl.write("Around 75 percent of people get a 7-10 percent increase to their salary when they job hop ")
        print("Around 75 percent of people get a 7-10 percent increase to their salary when they job hop")
        time.sleep(2)
        trtl.goto(-200,45)
        trtl.write("Do you like your current employment (yes/no) ")
        print("Do you like your current employment (yes/no)")
        answer = input("->")
        if answer.lower() == "yes":
         trtl.goto(-200,35)
         trtl.write("Consider asking for a raise around 50 percent of people who ask for a raise get one ")
         print("Consider asking for a raise around 50 percent of people who ask for a raise get one")
         time.sleep(2)
         trtl.goto(-200,25)
         trtl.write(" Its always good to have loyality to an employer as they can help you be promoted ")
         print(" Its always good to have loyality to an employer as they can help you be promoted ")
         time.sleep(3)
         wn.clear()
         wn.bgpic("up.gif")
         wn.update()
         playsound("king.mp3")
        elif answer.lower() == "no":
         trtl.goto(-200,35)
         trtl.write("Consider using another job offer as leverage to get a raise ")
         print("Consider using another job offer as leverage to get a raise ")
         time.sleep(2)
         trtl.goto(-200,25)
         trtl.write("You dont owe your employer anything so dont be afraid to burn bridges ")
         print("You dont owe your employer anything so dont be afraid to burn bridges")
         time.sleep(2)
         wn.clear()     
         wn.bgpic("explo.gif")
         wn.update()
         playsound("truth.mp3")

wn.mainloop()