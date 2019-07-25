let x1 = 3
let x2 = 18
let x3 = 6

let t = x3

console.log(`x1: ${x1}`, `x2: ${x2}`, `x3: ${x3}`)

x3 = x1
x1 = x2
x2 = t

console.log(`x1: ${x1}`, `x2: ${x2}`, `x3: ${x3}`)
