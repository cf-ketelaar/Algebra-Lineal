import sympy as sp

#imprima una matriz

A = sp.Matrix([[4,5,6],[1,2,3],[6,7,8]])
print('Imprima la matriz A: ', A)

#pprint (Imprime los objetos matemáticos de una manera profesional)
sp.pprint(A)


#Operaciones Elementales con Sympy
M = sp.Matrix([[1,1,1,850], [1,3,2,1625], [10,12,13,9725]])
sp.pprint(M)
print('\n Eliminación entradas debajo de la 1ra columna')
M1 =M.elementary_row_op('n->n+km',1,-1,0)
#sp.pprint(M1)
M2 =M1.elementary_row_op('n->n+km',2,-10,0)
sp.pprint(M2)
print('\n Eliminación entradas debajo de la 2da columna')
M3 =M2.elementary_row_op('n->n+km',2,-1,1)
#sp.pprint(M3)
M4 =M3.elementary_row_op('n->kn',2,1/2)
sp.pprint(M4)
print('\n Eliminación entradas arriba de la 3ra columna')
M5 =M4.elementary_row_op('n->n+km',0,-1,2)
M6 =M5.elementary_row_op('n->n+km',1,-1,2)
sp.pprint(M6)
print('\n Eliminación entradas arriba de la 2da columna')
M7= M6.elementary_row_op('n->kn',1,1/2)
M8= M7.elementary_row_op('n->n+km',0,-1,1)
sp.pprint(M8)



print('Resolución de un sistema de ecuaciones ')

A2 = sp.Matrix([[2,-5,2],[1,-1,1],[3,-6,3]])
b2 = sp.Matrix([0,0,0])

#x2 = A2.solve(b2)
#sp.pprint(x2)

#Resolución de un sistema de ecuaciones con Gauss Jordan
x2,param=A2.gauss_jordan_solve(b2)
#sp.pprint(x2)

print('Resolución del problema 1d')

A4 = sp.Matrix([[1,1,1,1],[1,2,2,3],[0,1,1,2],[1,-3,-3,-7]])
b4 = sp.Matrix([4,5,1,0])

x4,param = A4.gauss_jordan_solve(b4)

sp.pprint(x4)

print('Forma Escalonada reducida por renglones de una matriz con rref matriz 1d')
R4,pivotes =A4.rref()
sp.pprint(R4)

A5 = sp.Matrix([[1,1,1,1],[2,2,2,3],[0,1,3,2],[1,-3,-2,-7]])

print('\n Forma Escalonada por renglones matriz A4 modificada')
R5,pivotes =A5.rref()
sp.pprint(R5)

print('Ejercicios de Combinaciones Lineales')

U = sp.Matrix([[2,1],[-5,-1],[2,1]])
v = sp.Matrix([5,-11,5])
#v2= sp.Matrix([-1,-8 ,-1])

comb,params = U.gauss_jordan_solve(v)

sp.pprint(comb)

print('Ejercicio 2b, no hay combinación lineal')

U2 = sp.Matrix([[5,3,-2,3],[6,-2,-1,2],[3,-1,1,1],[5,3,0,3]])
v2 = sp.Matrix([[-6],[8],[2],[-6]])

#comb2,params = U2.gauss_jordan_solve(v2)

print('\nCompruebe que v2 no es combinación de los vectores con la FERR de U2')
U2v2 =U2.col_insert(4,v2)  #Matriz Aumentada

sp.pprint(U2v2)

R2,gustavo = U2v2.rref()

sp.pprint(R2)

