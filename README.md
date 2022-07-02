# RSA-HASH
El objetivo general del codigo implementado, es el de cifrar y decifrar mensajes, comprobando su validez, asi podemos evitar el ataque MAN IN THE MIDDLE, que intercepta el mensaje mediante el canal inseguro, incluyendo el tema de firmas digitales, mediante mapeo HASH. (RSA, DIFFIE-HELMAN)<br>
Se usan las funciones :<br>
- Fermat
- Euclides
- Euclides_Extendido
- Inverso de un numero
- Es_Compuesto
- MIller
- Randombits
- Randomgen
- RSA_KEY_GENERATOR
- Validador de firmas
<br>Primer ejercicio<br>
![image](https://user-images.githubusercontent.com/85748915/176943895-7c60f54a-cab8-4a20-b6a6-342929b315db.png)<br>
1) Primero se plantean las variables necesarias para realizar el ejercicio:
```python
e = 65537
n = 999630013489
phi_n = 999628013860
c = 747120213790
```
2) Segundo, se utiliza la Función Inversa para crear el valor d, tomando como valores para la función el phi_n* y el e:
```python
d = INVERSO(e,phi_n)
```
3) Luego, para poder obtener m, se aplicarán conceptos del Ataque de Texto Cifrado. Por lo cual se creará una variable x que sea coprimo con n, con la función EUCLIDES:
```python
for x in range(1,n):
  if EUCLIDES(x,n)==1:
    break
```
4) Despues, se crearán las variables c_, m_ y x_, los cuales simbolizan los valores de ```cx^e mod n```, la función descifrado de c_ y la inversa de x respectivamente:
```python
c_ = (c*Fermat(x,e,n))%n
m_ = Descifrado(c_,d,n)
x_ =INVERSO(x,n)
```
5) Ahora, con estos últimos 3 valores se puede realizar la obtención de m y la comprobación del cifreado m, si termina siendo el c planteado con anterioridad.
```python
m = (m_*x_)%n
p = Cifrado(m,e,n)
```
6) Finalmente, se imprime el m:
```python
print(m)
```
Segundo ejercicio<br>
![image](https://user-images.githubusercontent.com/85748915/176944006-45626b43-a69c-47f6-b0f4-11b5bab69ad4.png)<br>
Tercer ejecicio<br>
![image](https://user-images.githubusercontent.com/85748915/176944107-bf109294-3a4b-4727-b868-6c582aad7725.png)<br>
Importamos ramdon y hash, para poder trabajar con la firma digital<br>
![image](https://user-images.githubusercontent.com/85748915/177002659-77f9d0ef-d132-43cb-abeb-a10d73e987d6.png)<br>
Mediante la función RSA_KEY_GENERATOR, vamos a crear la variable ned de 32 bits<br>
![image](https://user-images.githubusercontent.com/85748915/177005825-8ce80411-aef7-4571-af6f-090559e35945.png)<br>
Crearemos la variable result con mapeo de HASH sha1 para codificar el mensaje, luego lo volveremos hexadecimal<br>
![image](https://user-images.githubusercontent.com/85748915/177005873-0f0175bc-5a29-49f8-b15a-7f527265ad34.png)<br>
Ahora pasaremos a crear la firma<br>
![image](https://user-images.githubusercontent.com/85748915/177005891-e11ff827-7cdf-429a-856c-71f9ea39e3c5.png)<br>
Obtenemos el mensaje mediante el cifrado<br>
![image](https://user-images.githubusercontent.com/85748915/177005918-eb70966a-d1d6-43ee-8321-783b4f0e6261.png)<br>
Procedemos a encriptar HASH<br>
![image](https://user-images.githubusercontent.com/85748915/177005950-91b165ca-12e8-4dd9-b35e-8556e09e3ee7.png)<br>
Por ultimo ingresamos los ultimos 3 mensajes para comprobar el programa<br>
![image](https://user-images.githubusercontent.com/85748915/177006006-ac0f5597-8caf-40c4-8831-f4bfacc0a610.png)<br>
Y asi termina el codigo


(*)Este valor fue obtenido del siguiente link: https://www.dcode.fr/euler-totient
