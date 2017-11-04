/**
 * Created by kit on 15.10.17.
 */

/**
* Created by kit on 15.10.17.
*/
function Add_to_basket_from_search() {
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
        url: "/select_product",
        cache: false,
        success: function(data) {
            $('#info-flover').html(data.content);
        },
        error: function (error) {
            alert(error)
        }
    });
    $('#overlay').fadeIn(400, function () {
        $('#info-flover')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 200);
    });
    return false;
}

$(document).ready(function() {
    $('#close_card, #overlay').click(function(){
        $('#info-flover')
            .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(400);
            }
        );
    });
});

