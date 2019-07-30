/**
 * Function takes 
 * @param {*} arr Array to be populated with multiples of m
 * @param {*} m Multiple
 * @param {*} n Number of multiples - must be a multiple of m
 */
function multiples (arr, m, n) {
    // For every iteration, add m to i until it reaches n
    for (let i = 1; i <= n; i++) {
        // Add i to the multiples array
        arr.push(i * m)
    }
}

let numbers = []
multiples(numbers, 4, 20)

console.log(numbers)