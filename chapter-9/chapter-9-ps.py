
import random

f=open("poem.txt")
content= f.read()
if("twinkel"in content):
    print("the word twinkel is present in the content ") 

else:
    print("the word twinkel is not present in the content ") 
f.close()



def game():
    print("you are playing a game...")

    score = random.randint(1, 100)
    print(f"your score is : {score}")

    # read highscore
    try:
        with open("highscore.txt", "r") as f:
            highscore = f.read()
            if highscore != "":
                highscore = int(highscore)
            else:
                highscore = 0
    except FileNotFoundError:
        highscore = 0

    # compare score
    if score > highscore:
        print("congratulations you have the highest score")
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
