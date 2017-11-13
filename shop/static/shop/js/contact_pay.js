/**
 * Created by kit on 20.10.17.
 */
$('#make-order-form').submit(function() {
        var phone = $('#contact_phone').val();
        var name = $('#contact_name').val();
        var address = $('#contact_address').val();
        $.ajax({
            type: "GET",
            url: "/contact_pay",
            data:{
                phone: phone,
                name: name,
                address: address
            },
            cache: false,
            success: function(data){
                $('#confirm_order').html(data.pay_set);
                $('#main_call_back')
                    .animate({opacity: 0, top: '45%'}, 100,
                    function(){
                    $(this).css('display', 'none');
                    }
                    );
                $('#confirm_order')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 100);
            },
            error: function (error) {
                alert(error)
            }
       });
    return false;
});

$(document).ready(function() {
    $('#close_card, #overlay').click(function(){
        $('#main_call_back')
            .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(100);
            }
        );
    });
});
