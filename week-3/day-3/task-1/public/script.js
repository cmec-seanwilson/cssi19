$(function () {
    const $addCityForm = $('#add-city-form')
    const $cityInputTemplate = $($addCityForm.find('template').html())
    $('#add-city-form #add-city').click(function () {
        $addCityForm.append($cityInputTemplate.clone())
    })

    $(document).on('click', '.remove-city', e => {
        const $cityInput = $(e.target).parent()
        $cityInput.remove()
    })

    $('#fav-cities .remove-city').click(e => {
        const $city = $(e.target).prev()
        const $removedCity = $(`<input type="hidden" name="removed_city[]" />`).val($city.text())
        $('#removed-cities').append($removedCity[0])
        $city.remove()
    })
})