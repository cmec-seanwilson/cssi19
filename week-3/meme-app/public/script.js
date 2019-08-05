$(function () {
    const $addLineButton = $('#add_line_btn')
    const $linesContainer = $('.lines')
    const $lineTemplate = $('#line-template')
    
    function createLine () {
        if ($('.lines').length >= 2) {
            return alert('You can only have a max of 2 lines')
        }
        const $line = $($lineTemplate.html())
        $linesContainer.append($line)
    }
    $addLineButton.click(createLine)
    
    $(document).on('click', '.remove_line_btn', function (e) {
        const $button = $(e.target)
        $button.parent().remove()
    })
})