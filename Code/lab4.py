with open("rosalind_ba5a.txt", "r") as file:
    # Read the entire file content
    money = int(file.readline().strip("\n"))
    coins = [int(c) for c in file.readline().strip("\n").split(",")]
