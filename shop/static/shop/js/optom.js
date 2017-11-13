/**
* Created by kit on 15.10.17.
*/
function optom() {
    $('#overlay').fadeIn(100,
            function () {
                $('#main_optom')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 100);
            });
}

$(document).ready(function() {
    $('#close_optom, #overlay').click(function(){
        $('#main_optom')
            .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(100);
            }
        );
    });
});
