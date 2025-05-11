document.addEventListener('click', valores)
document.querySelector('.clear').addEventListener('click', deletar)
document.querySelector('.item7').addEventListener('click', resolve)
document.querySelector('.DarkMode').addEventListener('click', DarkMode)

// variaveis 
let n1 = null
let n2 = null
let operador = ''
let display = document.querySelector('.display')


function valores(e) {
    if (e.target.classList.contains('numero')) {
        display.textContent += e.target.textContent
    } 
    else if(e.target.classList.contains('operador')) {
        n1 = parseFloat(display.textContent)

        n1 = parseFloat(display.textContent.replace(',', '.'))
        n2 = parseFloat(display.textContent.replace(',', '.'))
        operador = e.target.textContent
        display.textContent = ''
    } 
    else if(e.target.classList.contains('item2'))
    {
        if(!display.textContent.includes('.') && !display.textContent.includes(',')) 
        {
            display.textContent += e.target.textContent
        }
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
        console.log(resultado)
    }

    console.log(typeof(n1));
    console.log(typeof(n2));

    display.textContent = resultado.toFixed(1)
    n1 = parseFloat(resultado.toFixed(1))
    n2 = null
    operador = ''
}


function DarkMode() {
    const body = document.body

    if(body.classList.contains('dark')) {
        body.classList.remove('dark')
        body.classList.add('light')
    } else {
        body.classList.remove('light')
        body.classList.add('dark')
    }   
}