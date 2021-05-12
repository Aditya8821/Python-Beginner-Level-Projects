# Function to calculate the  
# electricity bill  
def calculateBill(units): 
  
    # Condition to find the charges  
    # bar in which the units consumed  
    # is fall  
    if (units <= 150): 
       
        return units * 5.50;  
      
    elif (151<=units<=300): 
      
        return ((150* 5.50) + 
                (units - 150) * 6);  
      
    elif (301<=units<=500): 
       
        return ((150 * 5.50) + 
                (150 * 6) + 
                (units - 300) * 6.5);  
      
    elif (units > 500): 
      
        return ((150 * 5.50) + 
                (150 * 6) + 
                (150 * 6.5) + 
                (units - 450) * 7);  
      
    return 0;

units=int(input("Enter Units Consumed:="))
print(calculateBill(units),"Rs Only\-")
  
