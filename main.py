from astro import gravitational_force

# Example: Earth and Moon
mass_earth = 5.972e24 # in kg
mass_moon = 7.348e22 # in kg
distance = 384_400_000 # in meters

force = gravitational_force(mass_earth, mass_moon, distance)
print(f"\nThe gravitational force between Earth and Moon is: {force:.2e} N")