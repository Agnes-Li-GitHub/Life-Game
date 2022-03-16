# Virtual Vending Machine
This is a vending machine that sells more than 1 types of drinks. The information is stored in a text (.txt) file with each line represents a type of soft drink. For each type of soft drink, the information is composed of the name of the soft drink, followed by the price, and the number of stocks, all separated by space.

### 4 main functions
##### 1. Insert
• It accepts a coin only. It reports the value of the inserted coin and the total amount of coin currently have.
##### 2. Reject
It rejects all the coins. It reports values of coin rejected in accending order and the total amount of coin rejected.
##### 3. Buy
It allows users to buy a drink and report the status of transaction and the amount of change. It only occurs when there are enough money in the machine. The program can also deal with cases of without enough credits and drinks are out of stock.
##### 4. Exit
It terminates the program by reporting the final inventory level.

### Program Flow
The program starts with user inputting the filename (in .txt) of the inventory list.
Then it shows all the drinks available, together with their prices and stock levels.
Afterwards, users can start to type commands (insert, reject, buy or exit) to perform different actions.

### Assumption
1. There are four types of coins ($1, $2, $5, $10) only.
2. User inputs are always valid.

FYI: This is a course assignment. 
