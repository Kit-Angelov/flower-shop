/**
 * Created by kit on 15.10.17.
 */
function OpenConstructor() {
	$.ajax({
        data: {},
        type: "GET",
        url: "/openconstructor",
        cache: false,
        success: function(data) {
        	$('#pack_constructor_wrap').html(data.packages_constructor);
            $('#scroll-basket-in-constructor').html(data.constructor_products);
            $('#scroll-in-consturctor').html(data.catalog_html);
            $('#final_sum_constructor').html(data.final_sum_constructor);
        },
        error: function (error) {
            alert(error)
        }
    });
	$('#overlay').fadeIn(400,
            function () {
                $('#constructor-wrapp')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
            });
    return false;
}

$(document).ready(function() {
	$('#close_constructor, #overlay').click(function(){
		$('#constructor-wrapp')
			.animate({opacity: 0, top: '45%'}, 200,
				function(){
					$(this).css('display', 'none');
					$('#overlay').fadeOut(400);
				}
			);
	});
});