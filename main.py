def path1m():
 print("You encountered a troll.")
 print("Enter 1 to fight it")
 print("Enter 2 to befriend it")
 in1 = input()

 if in1 == "1":
    print("You were defeated and died. Game Over")
  
 if in1 == "2":
    print("You befriend it and he helps you get home. You Won")

def path1r():
 print("You encountered a mermaid.")
 print("Enter 1 to fight it")
 print("Enter 2 to befriend it")
 in1 = input()

 if in1 == "1":
    print("You defeated her and was able to go home")
  
 if in1 == "2":
    print("You befriend it and she drowns. Game Over")


def welcome():
  print("Welcome to the Adventure Game. Select a path to get home.")
  print("Enter 1 to take the path to the mountain.")
  print("Enter 2 to take the path to the river.")
  in1 = input()

  if in1 == "1":
    path1m()
  
  if in1 == "2":
    path1r()

welcome()