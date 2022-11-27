#2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#⋁ - "Или"
#⋀ - "И"
#¬ - "Не"
X = Y = Z = True 
print(not (X or Y or Z) == ((not X) and (not Y) and (not Z)))

X = Y = Z = False 
print(not (X or Y or Z) == ((not X) and (not Y) and (not Z)))

X = True 
Y = Z = False
print(not (X or Y or Z) == ((not X) and (not Y) and (not Z)))

X = False 
Y = Z = True
print(not (X or Y or Z) == ((not X) and (not Y) and (not Z)))
