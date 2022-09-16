
def outer():
 outer_value= '外' 
 def inner():
  nonlocal outer_value 
  inner_value = '内'
  outer_value= "内側で変更" 
 inner() 
 return outer_value
 
 
 

value = outer() 
print(value) 


