let day = 100
window.onscroll = function () {
    day++
    let $h1 = document.createElement('h1')
    let date = new Date()
    date.setDate(date.getDate() + day)
    $h1.innerText = `Welcome to my amazing website on day ${date.toDateString()}`
    document.querySelector('body').append($h1)
}