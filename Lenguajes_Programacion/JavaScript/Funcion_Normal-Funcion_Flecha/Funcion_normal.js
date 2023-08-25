/*
//Funcion declarada 
function escribirhola () {
    console.log("Hola")
}
//invocacion de una funcion
escribirhola()

//////////////////////
function devuelvevalor () {
    console.log ("1")
    console.log ("2")
    console.log ("3")
    return "La funcion que retorna una cadena de texto"
}
console.log("1" + devuelvevalor())

let cadena_texto = devuelvevalor()
console.log("2" + cadena_texto)

///////////////////////////////
//Funcion con parametros 
function fparametros (nombre,result){
    console.log(`Soy una funcion con ${nombre}, y tengo como resultado ${result}`)
}
fparametros("Wilman", 18)
////////////////////////////
fdeclarada()
function fdeclarada (parameters) {
    console.log(" Esto es una funcion declarada")
}
fdeclarada()

//funcion anonima //Expresada
const functionexpresa = function () {
    console.log("Esto es una funcion expresiva, es decir una funcion que es almacenado en una constante")
}
functionexpresa()

// numeromayor()
// function numeromayor (num1,num2,num3) {
//     let contador = 0;
//     let contenedor_numeros = []
//     while (contador<3) {
//         let numeros = prompt("Ingrese tres numeros")
//         contenedor_numeros.push(numeros)
//         contador++
//     }
//     let numero_mayor = Math.max(num1,num2,num3)
//     console.log(`El numero mayor es ${numero_mayor}`)
//     console.log(contenedor_numeros)
// }

let num1 = prompt("Ingrese el numero 1")
let num2 = prompt("Ingrese el numero 2")
let num3 = prompt("Ingrese el numero 3")
numeromayor2(num1,num2,num3)

function numeromayor2 () {
    if ((num1 === num2) && (num1===num3)) {
        return console.log("Todos los numeros son iguales son iguales")
    } else {
        return console.log(Math.max(num1,num2,num3))
    }
}


*/


// let arrayVocales = ["a","e","i","o","u","A","E","I","O","U" ]

// let vocal_usuario = prompt("Ingrese una letra")
// esvocal(vocal_usuario)
// function esvocal() {
//     if (arrayVocales.includes(vocal_usuario)===true) {
//         console.log("Es una vocal")
//     } else {
//         console.log("No es una vocal")
//     }
// }

function xd (ite, cap){
    let a="";

    for(i=0; i<ite; i++){
        a=a+cap;
    }

    return a;
}

let parametrosNumero = prompt("digite un numero");
let parametersLetra = prompt("digite una letra");

console.log(xd(parametrosNumero, parametersLetra));