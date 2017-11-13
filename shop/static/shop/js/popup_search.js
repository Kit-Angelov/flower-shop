/**
 * Created by kit on 20.10.17.
 */
$('#search-form').submit(function() {
        var q = $('#search-product').val();
        var form = $(this).serialize();
        $.ajax({
            type: "GET",
            url: "/search",
            data:{
                form: form,
                q : q
            },
            cache: false,
            success: function(data){
                $('#search_global').html(data.search_set);
            },
            error: function (error) {
                alert(error)
            }
       });
        $('#overlay').fadeIn(100, function () {
        $('#search_global')
            .css('display', 'block')
            .animate({opacity: 1, top: '50%'}, 100);
        });
        return false;
    });

$(document).ready(function() {
    $('#close_search, #overlay').click( function(){
        $('#search_global')
        .animate({opacity: 0, top: '45%'}, 100,
            function(){
                $(this).css('display', 'none');
                $('#overlay').fadeOut(100);
            }
        );
    });
});