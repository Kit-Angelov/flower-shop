/**
 * Created by kit on 15.10.17.
 */
function func(data){
        $('#counter').html(data);
         document.getElementById('add_to_basket').innerHTML = '<div class="done_cl">' +
             '<p class="to_basket" id="to_basket">Перейти в корзину</p>' +
             '<p class="done" id="done">Продолжить покупки</p>' +
             '</div>';
         $('#done').click( function(){
		    $('#info-flover')
			.animate({opacity: 0, top: '45%'}, 200,
				function(){
					$(this).css('display', 'none');
					$('#overlay').fadeOut(400);
				}
			);
         });
         $('#to_basket').click( /*OpenBasket(),*/  function(){
		    $('#info-flover')
			.animate({opacity: 0, top: '45%'}, 200,
				function(){
					$(this).css('display', 'none');
				}
			);
		    $.ajax({
                data: {},
                type: "GET",
                url: "/basket",
                cache: false,
                success: function(data) {
                    $('#basket_full_main').html(data.basket_set);
                },
                error: function (error) {
                    alert(error)
                }
                });
                $('#basket_full_main')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
                return false;
            }
        );
    }
function Add_to_basket() {
    var pack = $('#pack').val();
    $.ajax({
        type: "GET",
        url: "/add_to_basket",
        data: {
            flower_count: $('#flower_count').val(),
            product_id: this.id,
            pack: pack
        },
        dataType: "html",
        cache: false,
        success: function (data) {
            func(data)
        }
    });
    return false;
}

