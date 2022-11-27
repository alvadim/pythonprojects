try_count = 0
try_max = 3
secret = 7
guess = 0
while try_count < try_max : #and guess != secret :
    guess = int(input("Guess the number 1 to 10 "))
    try_count += 1
    if guess > secret:
        print("Too much!")
    elif guess < secret :
        print("Less than...")
    else:
        print("Goal!!!")
        break
if guess != secret:
    print("You fail:(")
