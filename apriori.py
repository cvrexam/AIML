#!pip install apyori
 # Sample code to do Apriori in Python
import apyori
 # Creating Sample Transactions
transactions = [
     ['Milk', 'Bread', 'Saffron'],
     ['Milk', 'Saffron'],
     ['Bread', 'Saffron','Wafer'],
     ['Bread','Wafer'],
        ] 
 
# Generating association rules
Rules = list(apyori.apriori(transactions, min_support=0.5, min_confidence=0.5))
 
# Extracting rules from the object
for i in range(len(Rules)):
    LHS=list(Rules[i][2][0][0])
    RHS=list(Rules[i][2][0][1])
    support=Rules[i][1]
    confidence=Rules[i][2][0][2]
    lift=Rules[i][2][0][3]
    print("LHS:",LHS,"--","RHS:",RHS)
    print("Support:",support)
    print("Confidence:",confidence)
    print("Lift:",lift)
    print(10*"----")
