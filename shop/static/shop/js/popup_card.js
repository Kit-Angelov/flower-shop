/**
* Created by kit on 15.10.17.
*/
function SelectCard() {
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
        // var list = data.packages;
        //     list.forEach(function(element, i, list){
        //         alert("OK");
        //         alert(element.field.name);
        //
        //     })

            // var listitems;
            // $.each(temp, function(key, value){
            //     listitems += '<option value=' + key + '>' + value + '</option>';
            // });
            // $select.append(listitems);




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