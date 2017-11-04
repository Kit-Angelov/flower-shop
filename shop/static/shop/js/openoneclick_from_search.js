function Open_one_click_from_search() {
    $('#search_global')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
            }
        );
    var product_id = this.id;
    $.ajax({
        data: {
        product_id: product_id
        },
        type: "GET",
        url: "/select_product_one_click",
        cache: false,
        success: function(data) {
            $('#form_one_click').html(data.content);
        },
        error: function (error) {
            alert(error)
        }
    });
    $('#overlay').fadeIn(400, function () {
        $('#form_one_click')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 200);
    });
    return false;
}

$(document).ready(function() {
    $('#close_one_click, #overlay').click(function(){
        $('#form_one_click')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(400);
            }
        );
    });
});