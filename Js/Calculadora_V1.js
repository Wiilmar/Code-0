alert('Calculadora Experta');
let a = parseInt(prompt('Ingrese un numero'));
let operador = prompt('Ingrese un operador: [1]Multiplicacion [2]suma [3]Resta [4]Division');                        
let b = parseInt(prompt('ingrese otro numero'));
if (operador == '1'){
    resultado = (a*b)
    alert(`El resultado de la multiplicacion ${a} x ${b} es: ${resultado}`)
} else if (operador == '2') {
    resultado = (a+b)
    alert(`El resultado de la suma ${a} + ${b} es: ${resultado}`)
} else if (operador == '3') {
    resultado = (a-b)
    alert(`El resultado de la resta ${a} - ${b} es: ${resultado}`)
} else if (operador == '4') {
    resultado = (a/b)
    alert(`El resultado de la division de ${a} / ${b} es: ${resultado}`)
} else {
    alert(`Usted escogio un operador diferente al mostrado`)
}
    
