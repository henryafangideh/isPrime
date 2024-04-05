# Enter your code here. Read input from STDIN. Print output to STDOUT
numbers = []
t = int(input())

for i in range(t):
    n = int(input())
    numbers.append(n)



def isPrime(n):
    if n == 1:
        print('Not prime')
    elif n == 0:
        print('Not prime')
    elif n==2:
        print('Prime')
    elif n==3:
        print('Prime')
        
    else:
        count = 0
        times  = 0
        for i in range(1, n):
            if n % i == 0:
                count += 1
                if count > 2: #to break
                    print('Not prime')
                    break
        if count <= 2:
            print('Prime')
                
                
                
for _ in numbers:
    isPrime(_)
        

        
            
        
        
           
        
        
        
    
    
    
