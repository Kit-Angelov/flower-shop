/**
 * Created by kit on 20.10.17.
 */
$('#research-form').submit(function() {
        var q = $('#research-product').val();
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
        return false;
    });
