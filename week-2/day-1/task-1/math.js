function f (x) {
    return 3*x + 7
}

function g (x) {
    return 5*x + 5
}

function h (x) {
    return 5*(x**2) - 4*x + 2
}

function i (x, y) {
    return x**2 - y**2
}

function j (x, y, z) {
    return x + y + z
}

function k (r) {
    return 2 * Math.PI * r
}

function l (a, b, c) {
    return (-b + Math.sqrt(b**2 + 4*a*c)) / (2*a)
}

console.log(
    i(4, 3),
    i(3, 4)
)
