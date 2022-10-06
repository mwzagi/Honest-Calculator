import sys

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg == "":
        pass
    else:
        msg = msg_9 + msg
        print(msg)
        pass

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output

def msg_(msg_index):
    return msg[msg_index]

memory = 0
while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except:
        print(msg_1)
        continue
    else:
        if oper in ["+", "-", "*", "/"]:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            else:
                print(msg_3)
                continue
            print(result)
            
            while True:
                print(msg_4)
                answer = input()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_(msg_index))
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index = msg_index + 1
                                    continue
                                else:
                                    memory = result
                                    break       
                            else:
                                if answer == "n":
                                    break
                        
                    else:
                        memory = result
                else:
                    if answer != "n":
                        continue   
                while True:
                    print(msg_5)
                    answer = input()
                    if answer == "y":
                        break
                    else:
                        if answer == "n":
                            sys.exit()
                break              
        else:
            print(msg_2)