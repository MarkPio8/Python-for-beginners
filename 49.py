IsWeekend = False
print("Is weekend =",IsWeekend)

Temperature  = 25
print("Temperature = ",Temperature)

ToDoList = 'Shopping'
print("ToDoList =",ToDoList)

IsHappy  = IsWeekend and Temperature >= 20 and ToDoList ==''
print("IsHappy =",IsHappy)

IsHappy  = not IsWeekend and Temperature < 20 and ToDoList !=''
print("IsHappy =",IsHappy)

IsHappy  = IsWeekend and Temperature >= 20 and ToDoList =='' \
           or not IsWeekend and Temperature <20 and ToDoList !=''
print("IsHappy = ",IsHappy)
