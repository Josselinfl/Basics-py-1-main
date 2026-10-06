//Bienvenida a Javascript básico, para comentar una linea de código puedes usar las dos barras // y para comentar un bloque de varias líneas puedes usar barra y asterisco para abrir /*  asterisco y barra para cerrar */

//En el archivo index.html que tienes abierto en el navegador (preferiblemente chrome o firefox) vamos a trabajar con la consola, abre tu inspector y en la pestaña de consola, mira si puedes ver el mensaje escrito abajo.

console.log('Hola soy tu consola y juntas vamos a aprender Javascript')

//Si has encontrado el mensaje puedes continuar con los ejercicios

//Ejercicio 1: Imprime en la consola "Bienvenida/o al bootcamp Femcoders de Factoría F5" y mira en tu navegador si sale el resultado.

console.log("Bienvenida/o al bootcamp Femcoders de Factoría F5");


//VARIABLES Y TIPOS DE DATOS
//Ejercicio 2: Crea una variable por los siguientes tipos de dato: string, number, boolean, null, undefined, object, array e imprímelos en la consola.

const miString = "Hola, mundo";
const miNumber = 2026;
const miBoolean = true;
const miNull = null;

let miUndefined;

const miObject = {
  nombre: "IA",
  version: 4.0
};

const miArray = ["JavaScript", "Python", "C++"];

//Ejercicio 3: Crea una constante llamada postres con un tipo de dato array que contiene los siguientes elementos: helado, tarta, pastel e imprímelo en la consola. 

const postre = ["helado", "tarta", "pastel"];

console.log(postres);


//Ejercicio 4: Crea una constante con un tipo de dato objeto llamado coder que contengan dos propiedades, nombre y edad e imprímelo en la consola.

const coder = {
    nombre: "Ana",
    edad: 28
};

console.log(coder)


//Ejercicio 5: Busca como imprimir en consola el tipo de dato de cada variable que hemos creado.

let texto = "Hola Femcoders";

let numero = 2026;

let esBootcamp = true;

let valorNulo = null;

let valorNoDefinido;

let estudiante = {
    nombre: "María",
    edad: 25
};

let lenguajes = ["JavaScript", "HTML", "CSS"];

console.log(texto);
console.log(numero);
console.log(esBootcamp);
console.log(valorNulo);
console.log(valorNoDefinido);
console.log(estudiante);
console.log(lenguajes);


//OPERADORES ARITMÉTICOS
//Ejercicio 6: Crea una varible que sume 2 números e imprime el resultado en consola.

const num1 = Number(prompt("Introduce el primer número:"));
const num2 = Number(prompt("Introduce el segundo número:"));
const sumaInteractiva = num1 + num2;
console.log("El resultado de tu suma es:", sumaInteractiva);


//Ejercicio 7: Crea una varible que reste 2 números e imprime el resultado en consola.

//Escribe tu código aquí

const num3 = Number(prompt("Introduce el primer número:"));
const num4 = Number(prompt("Introduce el segundo número:"));
const restaInteractiva = num3 - num4;
console.log("El resultado de tu resta es:", restaInteractiva);


//Ejercicio 8: Crea una varible que multiplique 2 números e imprime el resultado en consola.

const num5 = Number(prompt("Introduce el primer número:"));
const num6 = Number(prompt("Introduce el segundo número:"));
const multiplicacionInteractiva = num5 * num6;
console.log("El resultado de tu multiplique es:", multiplicacionInteractiva);


//Ejercicio 9: Crea una varible que divida 2 números e imprime el resultado en consola.

const num7 = Number(prompt("Introduce el primer número:"));
const num8 = Number(prompt("Introduce el segundo número:"));
const dividaInteractiva = num3 / num4;
console.log("El resultado de tu divida es:", dividaInteractiva);




//OPERADORES DE COMPARACIÓN
// Ejercicio 10: Crea dos variables, la primera con valor 1 y la segunda con valor 2, compara ambas variables dentro de otra variable e imprime en la consola para ver el resultado.

const valor1 = Number(prompt("Introduce el primer número:"));
const valor2 = Number(prompt("Introduce el segundo número:"));

const sonDiferentes = valor1 < valor2;
console.log("¿Es el primer valor menor que el segundo?:", sonDiferentes);


// Ejercicio 10: Crea otra variable que compare las dos primeras variables creadas en el ejercicio anterior, para que el resultado impreso en la consola sea true.

const sonIguales = valor1 !== valor2;
console.log("¿Son valores distintos?:", sonIguales);


//Ejercicio 11: completa el ejercicio

let num11 = 15;
let num12 = 20;

let comparacion = num11 < num12
console.log(comparacion);


//Ejercicio 12: completa el ejercicio

let num13 = 1
let num3AsString = "1"

let result = num13 === num3AsString
console.log(result);

//Ejercicio 13: completa el ejercicio

let result2 = num13 ===num3AsString
console.log(result2)


//OPERADORES DE CADENAS
//Ejercicio 14: Crea una variable con tu nombre y otra variable con tu apellido y crea otra nueva variable con tu nombre completo concatenando las dos variables anteriores e imprime en consola. Debe haber un espacio entre tu nombre y apellido.

const nombre = "Josselin";
const apellido ="Flores";
const nombreCompleto = "nombre" + "apellido";

console.log(nombreCompleto);


//OPERADORES DE LÓGICA
//Ejercicio 15: Descomenta todo el bloque desde la variable 'a' hasta el 'console.log(res6)' y completa el ejercicio. (Saldrá un error y no podrás visualizar el resultado hasta que termines este ejercicio)

let a = 6;
let b = 3;

let res =  a < 10 && b > 1 //Eliminar el espacio "__" y coloca el comparador lógico que consideres para que el resultado sea true
console.log(res)

let res2 = a < 10 && b < 1 //Eliminar el espacio "__" y coloca el comparador lógico que consideres para que el resultado sea false
console.log(res2)

let res3 = a == 5 || b == 5 //Eliminar el espacio "__" y coloca el comparador lógico que consideres para que el resultado sea false
console.log(res3)

let res4 = a == 6 || b == 0 //Eliminar el espacio "__" y coloca el comparador lógico que consideres para que el resultado sea true
console.log(res4)

let res5 = a == 0 || b == 3 //Eliminar el espacio "__" y coloca el comparador lógico que consideres para que el resultado sea true
console.log(res5)

let res6 = a == 6 && b == 3 //Eliminar el espacio "__" y coloca el comparador lógico que consideres para que el resultado sea true
console.log(res6) 
