from os import name,system
colors={"red":"\033[31m","r":"\033[31m",
		"green":"\033[32m","g":"\033[32m",
		"yellow":"\033[33m","y":"\033[33m",
		"blue":"\033[34m","b":"\033[34m",
		"purple":"\033[35m","p":"\033[35m",
		"cyan":"\033[36m","c":"\033[36m",
		"white":"\033[37m","w":"\033[37m",
		"black":"\033[30m",
		"default":"\033[39m","d":"\033[39m"}

styles={"b":"\033[1m","i":"\033[3m","d":"\033[2m","s":"\033[4m",
	"t":"\033[9m","h":"\033[8m","B":"\033[22m","D":"\033[22m","I":"\033[23m","S":"\033[24m","T":"\033[29m","H":"\033[28m",
    "r":"\033[22;23;24;28;29m","R":"\033[0m"}

def div(string,sep=" "):
	if type(string)!=str or type(sep)!=str or len(sep)>1:
		error="wrong input (string!=str or sep!=chr)"
		raise TypeError(error)
	start=0
	array=[]
	for i in range(len(string)):
		if string[i]==sep:
			if i-start>0:
				array.append(string[start:i])
			start=i+1
	if start<len(string):
		array.append(string[start:])
	return array

def bin(a,typ=False):
	try:
		a=int(a)
		assert(type(typ)==bool)
	except:
		error="wrong input (decimal!=int or type != bool)"
		raise TypeError(error)
	s=""
	if a>=2:
		s=bin(a/2)
	if typ:
		return int(f"{s}{round(a%2)}")
	else:
		return f"{s}{round(a%2)}"

def cls():
	if name=="posix":
		system("clear")
	else:
		system("cls")

def rgb(r,g,b):
	try:
		r,g,b=int(r),int(g),int(b)
	except:
		error="wrong input (r,g,b!=int)"
		raise TypeError(error)
	if r>255 or r<0 or g>255 or g<0 or b>255 or b<0:
		error="rgb values out of range (0,255)"
		raise ValueError(error)
	else:
		return f"\033[38;2;{r};{g};{b}m"

def brgb(r,g,b):
	try:
		r,g,b=int(r),int(g),int(b)
	except:
		error="wrong input (r,g,b!=int)"
		raise TypeError(error)
	if r>255 or r<0 or g>255 or g<0 or b>255 or b<0:
		error="rgb values out of range (0,255)"
		raise ValueError(error)
	else:
		return f"\033[48;2;{r};{g};{b}m"

def style(*args):
	if len(args)==0:
		error="no arguments given"
		raise TypeError(error)
	elif len(args)==1:
		if type(args[0])!=str:
			error=f'"{args[0]}" is not a valid parameter'
			raise ValueError(error)
		else:
			it=args[0]
			typeit=False
	else:
		it=args
		typeit=True
	s=""
	for i in it:
		if i in styles:
			s=f"{s}{styles[i]}"
		elif i!=" " or i==" " and typeit:
			error=f'"{i}" is not a valid parameter'
			raise ValueError(error)
	return s

def color(a,st=None):
	if  type(a)!=str:
		error="wrong input (color != str)"
		raise TypeError(error)
	if a not in colors:
		error=f'"{a}" is not a color'
		raise ValueError(error)
	if st!=None:
		return colors[a]+st+colors["d"]
	else:
		return colors[a]


def ll(a):
	if type(a)!=list and type(a)!=tuple:
		error="Variable is not a list or a tuple"
		raise TypeError(error)
	li=[]
	for i in a:
		li.append(i)
	return li

def matriz(x,y,z=0):
	try:
		x,y=int(x),int(y)
	except:
		error="wrong input ('x' or 'y' != decimal)"
		raise TypeError(error)
	m=[]
	for i in range(x):
		a=[z]*y
		m.append(a)
	return m

def cursor(a=True):
	if type(a)!=bool:
		error="wrong input (parameter!=bool)"
		raise TypeError(error)
	if a:
		return "\033[?25l"
	else:
		return "\033[?25h"

#==============================================================

hpen=f"""{style('b')}"Unique Tools" {style('B')}is a python module that can help you insert ESC codes, solve python problems, simple functions that can be lazy to write over and over again and more interesting functions, here is a short guide to know its functions:

{style('b')}{rgb(230,220,100)}div{style('R')} .- This function does exactly what the native python function "split()" would do, except that it removes a slightly annoying property in some cases, for example:

	{color('b')}>>>{color('d')} text = {rgb(230,180,100)}"Hello world!"
	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}(text.{rgb(230,220,100)}split{color('d')}({rgb(230,180,100)} " " {color('d')}))
	{style('d')}['Hello','','','world!']{style('D')}

	As you can see, python creates empty strings when the character that defines the split point is repeated, div instead:
	
	{color('b')}>>>{color('d')} text = {rgb(230,180,100)}"Hello world!"
	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,220,100)}div{color('d')}(text))
	{style('d')}['Hello','world!']{style('D')}
	
	{style('b')}PARAMETERS:{style('B')} div(string,separation=" ")
	1. (string) can receive only text strings to be processed
	2. (separation) can only receive data of type "str" and not greater than 1 character, this will be the division point of the text string, by default it will have a value = " "
	
	{style('b')}RETURNS:{style('B')} a list with the text strings resulting from the division

{style('b')}{rgb(230,220,100)}bin{style('R')} .- This function is a recursive decimal to binary converter, so the extension of the number will depend on how big the base 10 decimal is. Example:

	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,220,100)}bin{color('d')}({rgb(100,220,150)}10{color('d')}))
	{style('d')}1010{style('D')}
	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,220,100)}bin{color('d')}({rgb(100,220,150)}50{color('d')}))
	{style('d')}110010{style('D')}
	
	{style('b')}PARAMETERS:{style('B')} bin(number,type=False)
	1. (number) can receive any type of data that can be converted to an integer, for example " {rgb(230,220,100)}bin{color('d')}({rgb(230,180,100)}'10'{color('d')}) ", this will be the number to convert to binary
	2. (type) can receive only boolean type values, this is an option to customize the output, when "type==True" the function will return an integer, when "type==False" the function will return a text string, by default it has the value of "False"
	
	{style('b')}RETURNS:{style('B')} an integer or a string with the decimal value converted to a binary number"""

#============================================================

hpes=f"""{style('b')}"Unique Tools" {style('B')}es un modulo de python que puede ayudarte, a insertar codigos ESC, resolver problemas de python, funciones simples que puede llegar a dar pereza escribir una y otra vez y mas funciones interesantes, aqui se resume una pequeña guia para conocer sus funciones:

{rgb(230,220,100)}{style('b')}div{style('R')} .- Esta funcion hace exactamente lo que haria la funcion nativa de python "split()" a excepcion de que elimina una propiedad un poco molesta en algunos casos, por ejemplo:
	
	{color('b')}>>>{color('d')} text = {rgb(230,180,100)}"¡Hola   mundo!"
	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}(text.{rgb(230,220,100)}split{color('d')}({rgb(230,180,100)} " " {color('d')}))
	{style('d')}['¡Hola','','','mundo!']{style('D')}
	
	como podras ver python crea cadenas vacias cuando el caracter que define el punto de division se repite, en cambio div:
	
	{color('b')}>>>{color('d')} text = {rgb(230,180,100)}"¡Hola   mundo!"
	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,220,100)}div{color('d')}(text))
	{style('d')}['¡Hola','mundo!']{style('D')}
	
	{style('b')}PARAMETROS:{style('B')} div(cadena,separacion=" ")
	1. (cadena) puede recibir unicamente cadenas de texto para ser procesadas
	2. (separacion) puede recibir unicamente datos de tipo "str" y no mayores a 1 caracter, este sera el punto de division de la cadena de texto, por defecto tendra un valor = " "
	
	{style('b')}RETORNA:{style('B')} una lista con las cadenas de texto resultantes de la division

{style('b')}{rgb(230,220,100)}bin{style('R')} .- Esta funcion es un conversor de decimal a binario de forma recursiva, por lo que la extension del numero dependera de que tan grande sea el decimal base 10. Ejemplo:

	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,220,100)}bin{color('d')}({rgb(100,220,150)}10{color('d')}))
	{style('d')}1010{style('D')}
	{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,220,100)}bin{color('d')}({rgb(100,220,150)}50{color('d')}))
	{style('d')}110010{style('D')}
	
	{style('b')}PARAMETROS:{style('B')} bin(numero,tipo=False)
	1. (numero) puede recibir cualquier tipo de dato que pueda convertirse en un entero, por ejemplo " {rgb(230,220,100)}bin{color('d')}({rgb(230,180,100)}'10'{color('d')}) ", este sera el numero a convertir en binario
	2. (tipo) puede recibir unicamente valores de tipo booleano, esta es una opcion para personalizar la salida, cuando "tipo==True" la funcion retornara un entero, cuando "tipo==False" la funcion retornara una cadena de texto, por defecto tiene el valor de "False"
	
	{style('b')}RETORNA:{style('B')} un entero o una cadena de texto con el valor decimal convertido en un numero binario
 
{style('b')}{rgb(230,220,100)}cls{style('R')} .- Esta funcion limpia la pantalla de tu terminal tanto en windows como en linux aunque puede que segun tu IDE no funcione de manera correcta por lo que es recomendable probarla antes, funciona usando la funcion "system()" del modulo "os", es una funcion ya conocida pero que aveces dapereza volver a escribir en cada programa que vas a usar. Ejemplo:

{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,180,100)} "hola" {color('d')})
{color('b')}>>>{color('d')} {rgb(230,220,100)}cls{color('d')}()
{color('b')}>>>{color('d')} {rgb(230,220,100)}print{color('d')}({rgb(230,180,100)} "mundo" {color('d')})
{style('d')}mundo{style('D')}

{style('b')}PARAMETROS:{style('B')} sin parametros.

{style('b')}RETORNA:{style('B')} None.

{style('b')}{rgb(230,220,100)}rgb, brgb{style('R')} .- Estas dos funciones son variaciones una de la otra, se utilizan para aplicar color a base de los codigos ESC y ANSI (mas informacion: {color('b')}https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#rgb-colors{color('d')}), como su nombre lo indica {style('b')}"rgb()" {style('B')}aplica color al texto en base a valores rgb (rojo, verde, azul) y {style('b')}"brgb()" {style('B')}utiliza el mismo principio pero aplicado al fondo del texto. Ejemplo:

>>> print(rgb(255,0,0),"¡Hola Mundo!")
¡Hola Mundo!

>>> print(brgb(255,0,0),"¡Hola Mundo!")
¡Hola Mundo!

PARAMETROS: 3 valores rgb donde: 0 >= r,g,b <=255. Puede recibir cualquier tipo de dato que pueda convertirse en un entero, por ejemplo: rgb("255","0","0").

RETORNA: Una cadena de texto corresponiente a la secuencia ESC con los valores rgb otorgados."""
	
def hp():
	while True:
		print(f'\t\t\t\t{style("b")}{rgb(126,66,245)}UNIQUE TOOLS{style("R")}\n')
		a=input('Type "en" for documenation in English or/o\nescribe "es" para documentacion en Español: ')
		cls()
		if a=="es":
			print(f'\t\t{style("b")}{rgb(126,66,245)}UNIQUE TOOLS{style("r")}\n\n{color("d")}{hpes}')
			break
		elif a=="en":
			print(f'\t\t{style("b")}{rgb(126,66,245)}UNIQUE TOOLS{style("r")}\n\n{color("d")}{hpen}')
			break
		else:
			print("wrong input try again:\n\n")