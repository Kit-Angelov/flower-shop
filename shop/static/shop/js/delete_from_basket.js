function delete_from_basket(){

        $.ajax({
            data: {
                elem_id: this.id
            },
            type: "GET",
            url: "/delete_from_basket",
            cache: false,
            success: function(data) {
                $('#basket_full_main').html(data.basket_set);
                $('#counter').html(data.basket_count);
            },
            error: function (error) {
                alert(error)
            }
        }
        );
        return false;
    }