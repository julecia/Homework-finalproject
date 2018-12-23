substring = " "
longest = " "

s = str(input("Please enter string to compare: "))
for i in range(0, len(s)):
    if s[i] >= substring[len(substring)-1]:
        substring += s[i]
    else:
        substring = " " + s[i]

    if len(substring) > len(longest):
        longest = substring
    print(substring)
print("Final substring:", longest[1:])