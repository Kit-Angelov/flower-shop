function add_product_to_basket_in_constructor() {
    var id = this.id;
    var count = $('.fieldCount' + id).val();
    var pack = $('#pack_constructor').val();
    $.ajax({
        type: "GET",
        url: "/add_to_basket_in_constructor",
        data: {
            product_id: id,
            count: count,
            pack_id: pack
        },
        cache: false,
        success: function(data) {
                $('#scroll-basket-in-constructor').html(data.constructor_products);
                $('#final_sum_constructor').html(data.final_sum_constructor);
            },
        error: function (error) {
            alert(error)
            }

    });
    return false;
}