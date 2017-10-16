/**
 * Created by kit on 15.10.17.
 */
function func(data){
        $('#counter').html(data);
        // document.getElementById('button-wrapp').innerHTML = '<div class="inner-text-product"><p>Добавлено в корзину</p></div>';
    }
function Add_to_basket() {
    $.ajax({
        type: "GET",
        url: "/add_to_basket",
        data: {
            flower_count: $('#flower_count').val(),
            product_id: this.id
        },
        dataType: "html",
        cache: false,
        success: function (data) {
            func(data)
        }
    });
    return false;
}