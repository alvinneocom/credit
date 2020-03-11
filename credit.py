"""
     ____                    __      __
    /\  _`\                 /\ \  __/\ \__
    \ \ \/\_\  _ __    __   \_\ \/\_\ \ ,_\
     \ \ \/_/_/\`'__\/'__`\ /'_` \/\ \ \ \/
      \ \ \L\ \ \ \//\  __//\ \L\ \ \ \ \ \_
       \ \____/\ \_\\ \____\ \___,_\ \_\ \__\
        \/___/  \/_/ \/____/\/__,_ /\/_/\/__/
    Alvin Rhaman
    Configurable credit card checker.
"""

from json import loads

# intput, reimplementation of get_int with try/catch
def intput(prompt):
    try:
        i = int(input(prompt))
        return i
    except Exception as e:
        return intput(prompt)

# die function
def die(n):
    print(n)
    exit(0)

# length of number
def length(n):
    return len(str(n))

# luhn verifier
def luhn(n):
    total = 0
    for i in range(length(n)):
        # dig is current digit
        dig = n % 10
        if(i % 2):
            dig *= 2
            total += (dig % 10) + (int(dig / 10))
        else:
            total += dig
        n = int(n / 10)
    return not(total % 10)

# makes sure n matches spec in m
def match(n, m):
    # acceptable length
    acclen = m["length"]
    # acceptable starting digits
    accstt = m["starting"]
    # spaghet
    return length(n) in acclen and int(str(n)[0:length(accstt[0])]) in accstt

def main():
    # get cc number
    num = intput("Number: ")
    # open dotfile, load config, then close dotfile
    dotfile = open("conf.json", "r")
    stds = loads(dotfile.read())["stds"]
    dotfile.close()
    # check number against all stds
    for i in range(len(stds)):
        std = stds[i]
        if luhn(num) and match(num, std):
            die(std["name"])
    # if it didn't die earlier, it's invalid
    die("INVALID")

main()
