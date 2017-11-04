function delete_from_lego_flower() {
    var id = this.id;
    var pack = $('#pack_constructor').val();
    $.ajax({
        type: "GET",
        url: "/delete_from_lego_flower",
        data: {
            elem_id: id,
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