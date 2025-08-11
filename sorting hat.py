# Inital house scores
Gryff = 0
Raven = 0
Huffle = 0
Sly = 0

# Used to initate and pose Question 1
Dawn = 1
Dusk = 2

print("Do you line Dawn or Dusk?")
print("1)Dawn")
print("2)Dusk")
q1 = int(input("Enter a number (1-2)"))

if q1 == 1:
  Gryff += 1
  Raven += 1

elif q1 == 2:
  Huffle += 2 
  Sly += 1

else:
  print("Wrong input")

# Used to initate and pose Question 2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
q2 = int(input("Enter 1-4: "))

if q2 == 1:
    Huffle += 2
elif q2 == 2:
    Sly += 2
elif q2 == 3:
    Raven += 2
elif q2 == 4:
    Gryff += 2
else:
    print("Wrong input.")

# Used to initate and pose Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
q3 = int(input("Enter 1-4: "))

if q3 == 1:
    Sly += 4
elif q3 == 2:
    Huffle += 4
elif q3 == 3:
    Raven += 4
elif q3 == 4:
    Gryff += 4
else:
    print("Wrong input.")

# Determine the winning house
houses = {
    "Gryffindor": Gryff,
    "Ravenclaw": Raven,
    "Hufflepuff": Huffle,
    "Slytherin": Sly
}

winning_house = max(houses, key=houses.get)

# Print final sorting hat scores
print("\nFinal House Scores:")
for house, score in houses.items():
    print(f"{house}: {score}")

print(f"\nThe Sorting Hat chooses... {winning_house}!")