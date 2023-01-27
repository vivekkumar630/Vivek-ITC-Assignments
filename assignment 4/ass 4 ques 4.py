candies = 0
found = False

# Loop through possible number of candies
for candies in range(1, 200):
    if candies % 5 == 2 and candies % 6 == 3 and candies % 7 == 2:
        candies = candies
        found = True
        break

# Print result
if found:
    print("The number of candies in the jar is: ", candies)
else:
    print("No solution found.")
