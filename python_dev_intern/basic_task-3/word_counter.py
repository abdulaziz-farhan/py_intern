try:
    with open(input("File name: ")) as f:
        print("Words:", len(f.read().split()))
except FileNotFoundError:
    print("File not found")