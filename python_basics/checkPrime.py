def checkPrime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5+1)):
        if a%i==0:
            return False
    return True

def main():
    num = int(input("Enter any number: "))
    if checkPrime(num):
        print("Prime")
    else:
        print("Not a prime")
        
if __name__ == "__main__":
    main()