# bug_hunt.py

count = 1
total = 0

# BUG: Missing colon (:) at the end of the while loop declaration. Fixed by adding ':'.
while count <= 5: # BUG: The condition was 'count < 5', which stopped at 4 and missed adding 5. Fixed by changing to '<=' or '< 6'.
    total = total + count
    count = count + 1

# BUG: Type mismatch error when concatenating a string and an integer. Fixed by wrapping total in str().
print("Sum of 1 to 5 is: " + str(total))