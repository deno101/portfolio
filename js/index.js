$(document).ready(function () {
    $('#icons a').click(function () {
        if ($(window).width() < 768) {
            $('#icons').css({'display': 'none'})
        }
    });

    $('#menu_icons').click(function () {
        if ($('#icons').css('display') === 'none') {
            $('#icons').css({'display': 'flex'})
        } else {
            $('#icons').css({'display': 'none'})
        }
    })

})