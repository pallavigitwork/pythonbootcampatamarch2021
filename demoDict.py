

demoDict =    {
  "Emp001": ("IronMan","CEO",23000000),
  "Emp002": ("BatMan","CTO",20000000),
  "Emp003": ("SuperWoman","CFO",18000000),
  }

#print(demoDict.get("Emp002")) #returns the value associated with the key

empIds={}
empIds=demoDict.keys()
print(empIds)
for emp in empIds:
    print(emp)
    print(demoDict.get(emp))
    