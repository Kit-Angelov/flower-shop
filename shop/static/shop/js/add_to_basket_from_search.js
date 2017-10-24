/**
 * Created by kit on 15.10.17.
 */
function func_search(data, id) {
    $('#counter').html(data);
    var ok_bask = document.getElementsByClassName('bask'+id);
    $(ok_bask).html('<p style="color: #b85778">В корзине</p>');

}
function Add_to_basket_from_search() {
    var pack = $('#pack').val();
    var id = this.id;
    $.ajax({
        type: "GET",
        url: "/add_to_basket",
        data: {
            flower_count: $('#flower_count').val(),
            product_id: id,
            pack: pack
        },
        dataType: "html",
        cache: false,
        success: function (data) {
            func_search(data, id)
        }
    });
    return false;
}

