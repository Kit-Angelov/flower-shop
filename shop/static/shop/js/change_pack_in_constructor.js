/**
 * Created by kit on 19.10.17.
 */
function change_pack_in_constructor(){
        var pack = $('#pack_constructor').val();
        $.ajax({
            data: {
                pack: pack
            },
            type: "GET",
            url: "/change_pack_in_constructor",
            cache: false,
            success: function(data) {
                $('#final_sum_constructor').html(data.final_sum_constructor);
            },
            error: function (error) {
                alert(error)
            }
        }
        );
        return false;
}
