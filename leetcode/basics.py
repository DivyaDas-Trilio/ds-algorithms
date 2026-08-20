def basics(inp):
    for i in range(inp):
        for j in range(inp):
            print("*", end="")
        print("")

if __name__ == "__main__":
    with open("/Users/divyajyotidas/workspace/input.txt", "r") as file:
        inp = file.read()
    basics(int(inp))