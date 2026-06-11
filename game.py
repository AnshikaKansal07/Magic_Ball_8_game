# Magic Ball is a fun future predictor that you can you to answer yes/no questions
import random as r
print("Welcome to magic ball 8 game!")
ans=[   
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."       
    ] 
while True:
    ques=input("Ask any question or enter quit to exit: ")
    if ques=="quit":
        break
    else:
        reply=r.randint(0,19)
        print(ans[reply])
print("Bye!!")