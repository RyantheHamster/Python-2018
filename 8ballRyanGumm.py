import random

def eightball():
    name = input("What is your name?")
    despacito = ""
    
    while despacito != "stop":
        despacito = input("Please ask a question.")
        answer = ["For sure %s!" % name, "That's possible %s." % name,
                  "NO WAY %s!" % name.upper(), "That's unlikely %s." % name,
                  "Not recommeneded %s..." % name, "Of course %s!" % name]
        if despacito != "stop":
            print(random.choice(answer))
        
eightball()
