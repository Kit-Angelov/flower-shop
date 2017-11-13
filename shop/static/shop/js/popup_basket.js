/**
* Created by kit on 15.10.17.
*/
function OpenBasket() {
    $.ajax({
        data: {},
        type: "GET",
        url: "/basket",
        cache: false,
        success: function(data) {
            $('#basket_full_main').html(data.basket_set);
        },
        error: function (error) {
            alert(error)
        }
    });
    $('#overlay').fadeIn(100, function () {
        $('#basket_full_main')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 100);
    });
    return false;
}

$(document).ready(function() {
    $('#close_basket, #overlay').click( function(){
        $('#basket_full_main')
        .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(100);
            }
        );
    });
});