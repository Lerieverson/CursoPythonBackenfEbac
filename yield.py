def counter_function():
  yield 1
  yield 2
  yield 3
  
contador = counter_function()
print(next(contador)) # Imprime 1
print(next(contador)) # Imprime 2
print(contador) # Imprime 3