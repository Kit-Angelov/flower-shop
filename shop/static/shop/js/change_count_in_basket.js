/**
 * Created by kit on 19.10.17.
 */
function change_count_in_basket(){
        var elem_id = this.id;
        var attr = this.value;
        $.ajax({
            data: {
                elem_id: elem_id,
                attr: attr
            },
            type: "GET",
            url: "/change_count_in_basket",
            cache: false,
            success: function(data) {
                $('#basket_full_main').html(data.basket_set);
            },
            error: function (error) {
                alert(error)
            }
        }
        );
        return false;
}

