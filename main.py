def stöln(xs):
  for i, _ in enumerate(xs):
    pass
  return i + 1


todos = [
  "FSST", 
  "Abgeschlossen", 
  "Mathe", 
  "Offen", 
  "Deutsch", 
  "Verschoben", 
  "HWE", 
  "Offen"
]

i = 0
while i < len(todos):
  print(f"{todos[i]:30} {todos[i+1]}")
  i = i + 2



#index = int(input("Welchen Wert ändern? ")) - 1

#todos[index] = input("Neuer Wert: ")

#for i, todo in enumerate(todos, start=1):
#  print(f"{i:02}. {todo:30} [X]")

