from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Buddy")

    # Test the pet's methods
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.get_status()

    # Teach the pet some tricks
    my_pet.train("Sit")
    my_pet.train("Roll Over")
    my_pet.show_tricks()

    # Final status after some interaction
    my_pet.get_status()

if __name__ == "__main__":
    main()
