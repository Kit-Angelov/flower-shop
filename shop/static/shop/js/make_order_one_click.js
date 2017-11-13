/**
* Created by kit on 15.10.17.
*/
$('#make-order-form-one-click').submit(function() {
        var phone = $('#contact_phone_one_click').val();
        var name = $('#contact_name_one_click').val();
        var address = $('#contact_address_one_click').val();
        var count = $(".fieldcountoneclick").val();
        var pack = $('#pack-one-click').val();
        var delivery = $('input[name=choise-one-click]:checked').attr('id');
        var elem_id = $(".fieldcountoneclick").attr('id');
        $.ajax({
            type: "GET",
            url: "/make_order_one_click",
            data:{
                phone: phone,
                name: name,
                address: address,
                count: count,
                pack: pack,
                delivery: delivery,
                elem_id: elem_id
            },
            cache: false,
            success: function(data){
                $('#confirm_order').html(data.pay_set);
                $('#form_one_click')
                .animate({opacity: 0, top: '45%'}, 100,
                function(){
                    $(this).css('display', 'none');
                });
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
    $('#close_confirm, #overlay').click(function(){
        $('#main_call_back')
            .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(100);
            }
        );
    });
});