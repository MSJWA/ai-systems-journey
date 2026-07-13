try:
    with open("data.txt") as file:
       content = file.read()
       print(content)
       if content.strip() == "":
            print("The file exists but it's empty.")
except FileNotFoundError:
    print("That file doesn't exist.")