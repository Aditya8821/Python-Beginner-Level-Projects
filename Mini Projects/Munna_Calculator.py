import sys
sys.path.append('/MyModules/')
import MyModules
from MyModules.mathy import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Enter your Query here=> ")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_num_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print("=>",r)
            except:
                print("Invalid Input")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
                
