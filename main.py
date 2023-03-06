todos = ["FSST", "Mathe", "Deutsch", "HWE"]

index = int(input("Welchen Wert ändern? ")) - 1

todos[index] = input("Neuer Wert: ")

i = 0 
while i < len(todos):
  print(f"{i+1}. {todos[i]}")
  i = i + 1


for i, todo in enumerate(todos, start=1):
  print(f"{i}. {todo}")
