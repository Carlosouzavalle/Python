document.addEventListener('click', valores)
document.querySelector('.clear').addEventListener('click', deletar)
document.querySelector('.item7').addEventListener('click', resolve)


// variaveis 
let n1 = null
let n2 = null
let operador = ''
let display = document.querySelector('.display')


function valores(e) {
    if (e.target.classList.contains('numero')) {

        display.textContent += e.target.textContent

    } else if(e.target.classList.contains('operador')) {
        n1 = parseFloat(display.textContent)
        operador = e.target.textContent
        display.textContent = ''
    }
} 


function deletar() {
    display.textContent = ''
    n1 = null
    n2 = null
    operador = ''
}

function resolve() {
    if (!operador || n1 === null) return

    n2 = parseFloat(display.textContent)
    let resultado = 0

    if(operador === '+') {
        resultado = n1 + n2
    } else if(operador === '-') {
        resultado = n1 - n2
    } else if(operador === '÷') {
        resultado = n1 / n2
    } else if(operador === 'x') {
        resultado = n1 * n2
    }


    display.textContent = resultado
    n1 = resultado
    n2 = null
    operador = ''
}