/**
 * Created by kit on 19.10.17.
 */
function change_pack_one_click(){
        var elem_id = $(".fieldcountoneclick").attr('id');
        var count = $(".fieldcountoneclick").val();
        var pack = $('#pack-one-click').val();
        var delivery = $('input[name=choise-one-click]:checked').attr('id');
        $.ajax({
            data: {
                elem_id: elem_id,
                count: count,
                pack: pack,
                delivery: delivery
            },
            type: "GET",
            url: "/change_pack_one_click",
            cache: false,
            success: function(data) {
                $('#form_one_click').html(data.one_click_info)
            },
            error: function (error) {
                alert(error)
            }
        }
        );
        return false;
}

