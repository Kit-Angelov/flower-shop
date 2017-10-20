/**
 * Created by kit on 19.10.17.
 */
function add_delivery(){
    var val = this.id;
    $.ajax({
        type: "GET",
        url: "/add_delivery",
        data: {
            val: val
        },
        dataType: "html",
        cache: false,
        success: function (data) {
            $('#final_sum').html(data);
        },
        error: function (error) {
                alert(error)
            }
    });
    return false;
}