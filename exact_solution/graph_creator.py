def main():
    n = 25
    print(n)
    for i in range(n):
        print(i, end=" ")
        for j in range(n):
            if j == i:
                continue
            else:
                print(j, end=" ")
        print()



if __name__ == "__main__":
    main()