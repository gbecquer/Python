print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = "TRUE"
love = "LOVE"

contador_true = 0
contador_love = 0

for i in range(len(true)):
    for j in range(len(name1)):
        if name1.lower()[j] == true.lower()[i]:
            contador_true += 1
        else:
            pass
    for k in range(len(name2)):
        if name2.lower()[k] == true.lower()[i]:
            contador_true += 1
        else:
            pass

for i in range(len(love)):
    for j in range(len(name1)):
        if name1.lower()[j] == love.lower()[i]:
            contador_love += 1
        else:
            pass
    for k in range(len(name2)):
        if name2.lower()[k] == love.lower()[i]:
            contador_love += 1
        else:
            pass


contador = str(contador_true) + str(contador_love)

if int(contador) > 90 or int(contador) < 10:
    print("Your score is " + contador + ", you go together like coke and mentos.")
elif int(contador) > 40 and int(contador) < 50:
    print("Your score is " + contador + ", you are alright together.")
else:
    print("Your score is " + contador + ".")



##########################################################################################
##########  Another way
##########################################################################################



print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = "TRUE"
love = "LOVE"

contador_true = 0
contador_love = 0

for i in range(len(true)):
    for j in range(len(name1)):
        contador_true += name1.lower()[j].count(true.lower()[i])

    for k in range(len(name2)):
        contador_true += name2.lower()[k].count(true.lower()[i])

for i in range(len(love)):
    for j in range(len(name1)):
        contador_love += name1.lower()[j].count(love.lower()[i])

    for k in range(len(name2)):
        contador_love += name2.lower()[k].count(love.lower()[i])



contador = str(contador_true) + str(contador_love)

if int(contador) > 90 or int(contador) < 10:
    print("Your score is " + contador + ", you go together like coke and mentos.")
elif int(contador) > 40 and int(contador) < 50:
    print("Your score is " + contador + ", you are alright together.")
else:
    print("Your score is " + contador + ".")