import json
from astro import gravitational_force

# Load the JSON file
with open("bodies.json", "r") as file:
  bodies = json.load(file)

mass_earth = bodies["earth"]
mass_moon = bodies["moon"]
distance = 384_400_000 # in meters

force = gravitational_force(mass_earth, mass_moon, distance)
print(f"\nThe gravitational force between Earth and Moon is: {force:.2e} N")
