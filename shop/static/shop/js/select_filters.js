/**
 * Created by kit on 15.10.17.
*/
function SelectFilters(){
    var category = $('#category').val();
    var sort = $('#sort').val();
    $.ajax({
        data: { category: category,
                sort: sort,
        },
        type: "GET",
        url: "/change_filters",
        cache: false,
        success: function(data) {
            $('#catalog_content').html(data.products_set);
        },
        error: function (error) {
            alert(error)
        }
    });
    return false;
}