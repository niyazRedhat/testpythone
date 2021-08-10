letter='''
Dear<|NAME|>
you are select
date<|DATE|>
'''
Name = input("enter your name")

Date = input("enter date")

letter = letter.replace("<|NAME|>",Name)

letter = letter.replace("<|DATE|>",Date)

print(letter)
