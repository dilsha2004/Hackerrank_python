def bonAppetit(bill, k, b):
    total = sum(bill) - bill[k]
    fair_share = total / 2
    if fair_share == b:
        print("Bon Appetit")
    else:
        print(int(b - fair_share))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
