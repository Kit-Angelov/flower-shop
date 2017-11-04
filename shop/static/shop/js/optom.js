/**
* Created by kit on 15.10.17.
*/
function optom() {
    $('#overlay').fadeIn(400,
            function () {
                $('#main_optom')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
            });
}

$(document).ready(function() {
    $('#close_optom, #overlay').click(function(){
        $('#main_optom')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(400);
            }
        );
    });
});
