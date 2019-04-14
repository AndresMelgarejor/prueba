from sympy import*
x,y,z=symbols('x,y,z')
#print(sqrt(8))

#reemplzar una variable
"""
print((1 + x*y).subs(x, pi))
(1 + x*y).subs({x:pi, y:2})
print((x**2 + x**4).subs(x**2, y))
"""
#como reemplzar un parte especifica
"""
print((1 + x*y).xreplace({x: pi}))
print((1 + x*y).xreplace({x: pi, y: 2}))
print((x**2 + x**4).xreplace({x**2: y}))
"""
#evaluar simultaneamente 
"""
print((x/y).subs([(x, 0), (y, 0)]))
print((x/y).subs([(x, 0), (y, 0)], simultaneous=True))
print(((x + y)/y).subs({x + y: y, y: x + y}))
print(((x + y)/y).subs({x + y: y, y: x + y}, simultaneous=True))
"""
#si deseamos evaluar una expresión usamos evalf dentro de subs
"""
print((1/x).evalf(subs={x: 3.0}, n=10))
#otra forma
print(N(sqrt(2)*pi, 5))
"""
#llamar una funcion anonima
"""
f = Lambda(x, x**2)
print(f(4))
"""

#obtener el valor numerico de una variable predefiida
# float(pi)

#estas seran atualizaciones de codigo realizadas por Git
"""
Acá esta este comentario de prueba
"""
#aca estoy probando el nuevo commit
"""
luego de hacer el push realicé este comentario
"""

#tercer commit con vs
