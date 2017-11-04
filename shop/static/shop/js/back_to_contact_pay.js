/**
* Created by kit on 15.10.17.
*/
function back_to_contact_pay() {
        $('#confirm_order')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
            }
        );
        $('#main_call_back')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 200);
}

$(document).ready(function() {
    $('#close_basket, #overlay').click(function(){
        $('#main_call_back')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(400);
            }
        );
    });
});