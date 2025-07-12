
#جواب های استاد
x = []
# جواب های دانشجو
y = []
def question():
    true = 0
    for i in range(0, 4):
        ask1 = input("enter teachers correct answer \n")
        x.append(ask1)
    for i in range(0, 4):
        ask2 = input("enter students answer")
        y.append(ask2)
    if x[0] == y[0]:
        true = true + 5
    if x[1] == y[1]:
        true = true + 5
    if x[2] == y[2]:
        true = true + 5
    if x[3] == y[3]:
        true = true + 5
    if true >= 10:
        print(f"your mark is {true} you are passed")
    elif true < 10:
        print("you are lose")
question()


