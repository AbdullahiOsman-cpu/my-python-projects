# A simple backend script to save data to a file
user_name = input("Enter a name to save: ")

# This opens (or creates) a file called data.txt and adds the name
with open("data.txt", "a") as file:
    file.write(user_name + "\n")

print(f"Success! {user_name} has been saved to the database.")

