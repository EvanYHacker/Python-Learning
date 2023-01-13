import random

low_number=1
high_number=random.randint(10,1000)
number = random.randint(low_number,high_number)

new_low=low_number
new_high=high_number

guess_count=1
guess=0
while guess==0:
    try:
        guess = int(input(f"Guess a number between {low_number} and {high_number}\n"))
    except ValueError:
        print("This is not a valid number")    

while guess!=number:
    if guess>number:
        if guess<high_number:
            new_high=guess
        try:
            guess=int(input(f"{guess} is too high, guess a lower number\n  Hint: You now know it is between {new_low} and {new_high}\n"))
        except ValueError:
            print("This is not a valid number")
        guess_count+=1
       
    else:
        if guess>low_number:
            new_low=guess
        try:
            guess=int(input(f"{guess} is too low, guess a higher number\n  Hint: You now know it is between {new_low} and {new_high}\n"))
        except ValueError:
            print("This is not a valid number")
        guess_count+=1

if guess_count==1:
    print(f"Yes! The number is {number}! It only took you ONE guess!") 
else:
    print(f"Yes! The number is {number} - it took you {guess_count} guesses to find it.\n")            

#user can still guess NaN
#user can guess a number out of range - it wont ruin guess count or hint - but find a better solution
#