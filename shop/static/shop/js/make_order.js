/**
* Created by kit on 15.10.17.
*/
function make_order() {
        var delivery = $('input[name=choise]:checked').attr('id');
        var value = 'delivery1';
        $('#basket_full_main')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
            }
        );

        if (delivery === value){
            $('#contact_address').css('display', 'none')
        }
        else {
            $('#contact_address').css('display', 'block')
        }

        $('#main_call_back')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 200);
}

$(document).ready(function() {
    $('#close_call_back, #overlay').click(function(){
        $('#main_call_back')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(400);
            }
        );
    });
});
