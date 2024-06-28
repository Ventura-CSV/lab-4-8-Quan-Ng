def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
    
        div = 3
        while div * div <= num:
            if num % div == 0:
                return False
            div += 2
        
        return True
    
    def find_primes(begin, end):
        
        for num in range(begin, end + 1):
            if is_prime(num):
                plist.append(num)
                
        return plist
    
    while True:
        try:
            begin = int(input("Enter first number(greater than 1): "))
            end = int(input("Enter second number(must be greater than 1 and the first number): "))
        
            if begin <= 1 or end <= 1:
                print("both numbers must be greater than one")
                continue
            if begin >= end:
                print("The Second number must be greater than the first number.")
                continue
            
            break
        except ValueError:
            print("Invalid input")
        
    plist = find_primes(begin, end)
    print(" ".join(map(str,plist)))
                





    return plist


if __name__ == '__main__':
    main()
