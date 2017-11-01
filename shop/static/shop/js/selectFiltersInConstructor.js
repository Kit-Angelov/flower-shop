/**
 * Created by kit on 15.10.17.
*/
function SelectFilterInConstructor(){
    var category = $('#category_in_constructor').val();
    $.ajax({
        data: {
            category: category
        },
        type: "GET",
        url: "/change_filters_in_constructor",
        cache: false,
        success: function(data) {
            $('#scroll-in-consturctor').html(data.products_set);
        },
        error: function (error) {
            alert(error)
        }
    });
    return false;
}