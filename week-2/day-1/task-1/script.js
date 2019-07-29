for (let i = 0; i <= 10; i++) console.log(i)

let result = prompt('Enter your name:\n')
console.log('Hello,', result)
alert(`Hello, ${result}`)

function isPassing (score) {
    let passing = false
    if (score >= 57) passing = true

    return passing
}

function start () {
    const score = parseInt(prompt('What score did you get on your math test?'))
    if (isNaN(score)) {
        alert('Enter a real number man!') 
        return start()
    }
    else alert(isPassing(score) ? `Great! Your score of ${score} is a passing one!` : `Sorry! You're score of ${score} is an utter failure`)
}

start()