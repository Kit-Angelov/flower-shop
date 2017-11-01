/**
 * Created by kit on 20.10.17.
 */

$('#call_back_form').submit(function() {
        var form = $(this).serialize();
        $.ajax({
            type: "GET",
            url: "/make_order",
            data:{
                form: form
            },
            cache: false,
            success: function(){
                popup_pay();
            },
            error: function (error) {
                alert(error)
            }
       });
        $('#main_call_back')
        .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
            }
        );
        $('#')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 200);
        return false;
        });
