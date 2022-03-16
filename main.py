def insert(n): 
    x = 'Inserted a $z coin. '
    x = x.replace('z',n)
    global total
    total = int(n) + total
    print(x+'$'+ str(total) + ' in Total.')

def reject(n):
    for i in range(len(n)): #change to int 
        n[i] = int(n[i])
    if len(n) == 0:
        print('Rejected no coin!')   
    else:
        n.sort()
        a = 0 #caculate the total amount
        for i in n:
            a = a + i
        for i in range(len(n)):
            n[i] = '$' + str(n[i])# n =[$2,$3,$4]
        y=''
        for i in n: #getting all $X out 
            y = y + i + ', '
        y = y[0:len(y)-2] #to ignore the last space and ,
        print1 = 'Rejected z. '
        print1 = print1.replace('z', y)
        print2 = '$z in Total.'
        print2 = print2.replace('z', str(a))
        print(print1 + print2)

def buy(n,drinks):
    global total
    global reject_total
    for i in range(len(drinks)):
        if drinks[i][0] in n:
            if total >= int(drinks[i][1]) and int(drinks[i][2]) !=0: # have stock + money
                x = 'Paid $z. '
                x = x.replace('z', str(total))
                y = 'Returned $z change.'
                value = total - int(drinks[i][1])
                
                if value == 0:   
                    y = y.replace('$z', 'no')
                    print('Dropped ' + drinks[i][0]+'. ' + x + y)
                    total = 0
                    reject_total=[]
                    drinks[i][2] = int(drinks[i][2]) - 1
                    break
                    
                else:
                    y = y.replace('z', str(value))
                    print('Dropped ' + drinks[i][0]+'. ' + x + y)
                    total = 0
                    reject_total=[]
                    drinks[i][2] = int(drinks[i][2]) - 1
                    break
                    
            if int(drinks[i][2]) == 0: #no stock and have money
                print(drinks[i][0] + ' is out of stock!')
                break
            
            else: #no money
                x = 'Inserted $z but needs $y.'
                x = x.replace('z', str(total))
                x = x.replace('y', drinks[i][1])
                print('Not enough credit to buy '+ drinks[i][0]+'! '+x)
                break
                  
        else:
            pass
              
#the program starts at here
print('File to initialize the vending machine:')
user = input() 
file = open(user,'r')
count = 0

for i in file:
    count = count + 1 #count how many lines -> drinks
    Inventory = 'Inventory: z type(s) of soft drinks available'
    Inventory = Inventory.replace("z", str(count))
file.close
print(Inventory)

drinks=[]
file = open(user,'r')
final = []
for i in file:
    semi_final = []
    y = i.strip()
    y = y.split(' ')
    alist =[y[0], y[1], y[2]]
    drinks.append(alist)
    print('Name: '+y[0], 'Price: $'+y[1],'Stock: '+y[2], sep=', ',end='\n')
#print(drinks) -> [[cocacola, $5, 5], [fanta, $3, 4]]

#here starts user input command
total = 0
reject_total = []
while True:
    n = input()    
    if 'Insert' in n:
        n = n.split(' ')
        reject_total.append(n[1])
        insert(n[1]) # only 5
    if n == 'Reject':
        reject(reject_total)#[3,5,2] not organised
        reject_total = [] #clear everything
        total = 0
    if 'Buy' in n:
        buy(n,drinks)
    if n == 'Exit':
        print(Inventory)
        for i in range(count):
            print('Name: '+drinks[i][0], 'Price: $'+drinks[i][1],'Stock: '+str(drinks[i][2]), sep=', ',end='\n')
        break
