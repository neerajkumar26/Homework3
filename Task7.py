# Name: - Neeraj Kumar
# ID: - 2047559
mydict = {}

print("Enter player 1's jersey number:", end ="\n")
num = int(input())
print("Enter player 1's rating:",end ="\n")
mydict[num] = int(input())
print()

print("Enter player 2's jersey number:",end ="\n")
num = int(input())
print("Enter player 2's rating:",end ="\n")
mydict[num] = int(input())
print()

print("Enter player 3's jersey number:",end ="\n")
num = int(input())
print("Enter player 3's rating:",end ="\n")
mydict[num] = int(input())
print()

print("Enter player 4's jersey number:",end ="\n")
num = int(input())
print("Enter player 4's rating:",end ="\n")
mydict[num] = int(input())
print()

print("Enter player 5's jersey number:",end ="\n")
num = int(input())
print("Enter player 5's rating:",end ="\n")
mydict[num] = int(input())
print()

print("ROSTER")
arr = []
for key in mydict:
    arr.append(key)
    pass
arr.sort()
for key in arr:
    print(f"Jersey number: {key}, Rating: {mydict[key]}")

opt = ""

while opt != "q":
    print()
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    print("Choose an option:")
    opt = input()
    if opt == "a":
        print("Enter a new player's jersey number:")
        num = int(input())
        print("Enter the player's rating:")
        mydict[num] = int(input())
        arr.append(num)
        arr.sort()
    elif opt == "u":
        print("Enter a jersey number:")
        num = int(input())
        print("Enter a new rating for player:")
        if num in arr:
            mydict[num] = int(input())
            pass
    elif opt == "r":
        print("Enter a rating:")
        rate = int(input())
        print()
        print(f"ABOVE {rate}")
        for key in arr:
            if mydict[key] > rate:
                print(f"Jersey number: {key}, Rating: {mydict[key]}")
                pass
            pass
    elif opt == "o":
        print("ROSTER")
        for key in arr:
            print(f"Jersey number: {key}, Rating: {mydict[key]}")
            pass
    elif opt == "d":
        print("Enter a jersey number:")
        num = int(input())
        arr.remove(num)
        mydict.pop(num)
