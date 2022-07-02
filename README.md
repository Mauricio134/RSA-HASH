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
(*)Este valor fue obtenido del siguiente link: https://www.dcode.fr/euler-totient
