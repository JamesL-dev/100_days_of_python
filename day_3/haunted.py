print('''
88                                                                       88  
88                                              ,d                       88  
88                                              88                       88  
88,dPPYba,  ,adPPYYba, 88       88 8b,dPPYba, MM88MMM ,adPPYba,  ,adPPYb,88  
88P'    "8a ""     `Y8 88       88 88P'   `"8a  88   a8P_____88 a8"    `Y88  
88       88 ,adPPPPP88 88       88 88       88  88   8PP""""""" 8b       88  
88       88 88,    ,88 "8a,   ,a88 88       88  88,  "8b,   ,aa "8a,   ,d88  
88       88 `"8bbdP"Y8  `"YbbdP'Y8 88       88  "Y888 `"Ybbd8"'  `"8bbdP"Y8 
      ''')
print("Welcome to Haunted. A choose your own adventure game.\n")
choice1 = input("Would you like to begin? Enter y/n\n")
if (choice1 == 'y'):
    print('''
                                                 ,           ^'^  _
                                              )               (_) ^'^
                                 .---------. ((        ^'^
                                  `'`'`'`'`( ||                 ^'^
                                /`'`'`'`'`'`\||           ^'^
                               /`'`'`'`'`'`'`\|
                       ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
                  /_____________\ |")| |  |  |/ |_| \|
                   |  __   __  |  '==' '=='  /_______\  
                   | /  \ /  \ |   _______   |,^, ,^,|    
                   | |--| |--| |  ((--.--))  ||_| |_||   
     _      _      | |__| |("| |  ||  |  ||  |,-, ,-,|  
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,ldb
    \n''')
    print("You find yourself on the rainslick precipice of the house on the hill. You have heard stories that the house was haunted.\n")
else:
    print("Game over\n")
    print("You turn around and leave. To die another day.\n")

choice2 = input("Do you want to enter the house? Enter y/n\n")
if (choice2 == 'y'):
    print("The door creaks open slowly as you press your hand on its surface. You are enveloped in a cold musty stench as if the house lets out a dying breath\ndisturbed by your presence.")
else:
    print("Too spooky. You get the hell out of there.\n")
    print("Game Over")
    
