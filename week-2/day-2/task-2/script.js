// function getNumber () {
//     let ask = () => parseInt(prompt('Enter a number'))
//     while (isNaN(ask())) {
//         ask()
//     }

//     alert('Nice number!')
// }

// getNumber()

function getNumber ()  {
    let input = prompt('Enter a number')
    let number = parseInt(input)
    if (isNaN(number)) {
        document.write('Horrible Tries: ' + input + '<br>')
        return getNumber()
    } else {
        return number
    }
}

let number = getNumber()
alert(number + 10)