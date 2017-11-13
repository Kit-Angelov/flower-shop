/**
* Created by kit on 15.10.17.
*/
function back_to_one_click() {
        $('#confirm_order')
            .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
            }
        );
        $('#form_one_click')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 100);
}

$(document).ready(function() {
    $('#close_one_click, #overlay').click(function(){
        $('#form_one_click')
            .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(100);
            }
        );
    });
});
