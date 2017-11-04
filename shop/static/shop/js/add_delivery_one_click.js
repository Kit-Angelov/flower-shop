/**
 * Created by kit on 19.10.17.
 */
function add_delivery_one_click(){
        var elem_id = $(".fieldcountoneclick").attr('id');
        var count = $(".fieldcountoneclick").val();
        var pack = $('#pack-one-click').val();
        var delivery = this.id;
        var value = 'delivery1';
        $.ajax({
            data: {
                elem_id: elem_id,
                count: count,
                pack: pack,
                delivery: delivery
            },
            type: "GET",
            url: "/add_delivery_one_click",
            cache: false,
            success: function(data) {
                $('#form_one_click').html(data.one_click_info)
                if (delivery === value){
                    $('#contact_address_one_click').css('display', 'none')
                }
                else {
                    $('#contact_address_one_click').css('display', 'block')
                }
            },
            error: function (error) {
                alert(error)
            }
        }
        );
        return false;
}

