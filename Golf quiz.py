ready = input("Are you ready to test your golf trivia knowledge? (Yes/No): ").strip().capitalize()
total = 0

if ready == "Yes":
    print("Great!")
    print()

else:
    exit()

question1 = input("""Question 1:
Who won the most majors?

A. Tiger Woods
B. Jack Nicklaus
C. Ben Hogan
D. Gene Sarazan
""").strip().capitalize()

if question1 == "B":
    total += 1


print()
question2 = input("""Question 2:
As at 2010, how many majors has Tiger Woods won?

A. 12
B. 13
C. 14
D. 15
""").strip().capitalize()

if question2 == "C":
    total +=1
    
print()
question3 = input("""Question 3:
What country is Gary Player from?

A. South Africa
B. USA
C. Australia
D. Germamy
""").strip().capitalize()


if question3 == "A":
    total +=1
    
print()
question4 = input("""Question 4:
When was the first Ryder Cup played?

A. 1924
B. 1927
C. 1934
D. 1937
""").strip().capitalize()

if question4 == "B":
    total +=1
    
print()
question5 = input("""Question 5:
Where did golf originate from?

A. England
B. Netherlands
C. Scottland
D. USA
""").strip().capitalize()

if question5 == "C":
    total +=1

print()
question6 = input("""Question 6:
We all know first and second,
but do you know who has the THIRD most wins at the Majors?

A. Ben Hogan
B. Tom Watson
C. Walter Hagen
D. Gary Player
""").strip().capitalize()

if question6 == "C":
    total +=1

print()
question7 = input("""Question 7:
When did the PGA European Tour come into existence?

A. May 12, 1974
B. April 22, 1974
C. May 22, 1972
D. April 12, 1972
""").strip().capitalize()

if question7 == "D":
    total +=1

print()
question8 = input("""Question 8:
How much does the standard golf ball weigh?

A. 1.62 ounces
B. 1.67 ounces
C. 1.72 ounces
D. 1.77 ounces
""").strip().capitalize()

if question8 == "A":
    total +=1

print()
question9 = input("""Question 9:
Tiger Woods won the British Open in 2000.
Which course was it played on?

A. Muirfield
B. St. Andrews
C. Royal Troon Golf Club
D. Carnoustie Golf Links
""").strip().capitalize()

if question9 == "B":
    total +=1
    
print()
question10 = input("""Question 10:
What is the only Major that Sam Snead didn't win in his career?

A. Masters 
B. British Open
C. PGA Championship
D. US Open
""").strip().capitalize()

if question10 == "D":
    total +=1

print()
question11 = input("""Last question!
In 2010, Who ended Tiger Woods' 5 year reign as number 1 golfer in the world?

A. Lee Westwood
B. Rory Mcllroy
C. Greg Norman
D. Dustin Johnson
""").strip().capitalize()


if question11 == "A":
    total +=1


perc = total / 11
percentage = round(perc,2)
right = int(percentage *100)

print()
print("Thank you for playing!")
print(f"You got {right} % correct! :) ")


qna = """Question 1: Who won the most majors?
B. Jack Nicklaus

Question2: As at 2010, how many majors has Tiger Woods won?
C. 14

Question 3: What country is Gary Player from?
A.South Africa

Question 4: When was the first Ryder Cup played?
B. 1927

Question 5: Where did golf originate from?
C. Scottland

Question 6: Who has the THIRD most wins at the Majors?
C. Walter Hagen

Question 7: When did the PGA European Tour come into existence?
D. April 12, 1972

Question 8: How much does the standard golf ball weigh?
A. 1.62 ounces

Question 9: Tiger Woods won the British Open in 2000.
Which course was it played on?
B. St. Andrews

Question 10: What is the only Major that Sam Snead didn't win in his career?
D. US Open

Question 11/ Last question:
In 2010, Who ended Tiger Woods' 5 year reign as number 1 golfer in the world?
A. Lee Westwood

"""
answers = input("Would you like to see the correct answers? (Yes/No): ").strip().capitalize()
print()

if answers == "Yes":
    print()
    print (qna)
    quit

else:
    quit


