def physics(m):
    c = 300000000 
    energy = m * c ** 2
    return energy



def main():
    mass = int(input("Enter a mass: "))
    result = physics(mass)
    print("Energy: ", result)

main()
