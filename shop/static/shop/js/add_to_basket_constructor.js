/**
 * Created by kit on 15.10.17.
 */
function func_close_constructor(data) {
    $('#counter').html(data);
    $('#constructor-wrapp')
        .animate({opacity: 0, top: '45%'}, 200,
            function(){
                $(this).css('display', 'none');
            }
        );
    $('#closing_constructor')
        .css('display', 'block')
        .animate({opacity: 1, top: '50%'}, 200);


}
$(document).ready(function() {
	$('#close_constructor, #overlay').click(function(){
		$('#closing_constructor')
			.animate({opacity: 0, top: '45%'}, 200,
				function(){
					$(this).css('display', 'none');
					$('#overlay').fadeOut(400);
				}
			);
	});
});

function add_to_basket_constructor() {
    var pack = $('#pack_constructor').val();
    $.ajax({
        type: "GET",
        url: "/add_to_basket_constructor",
        data: {
            pack_id: pack
        },
        dataType: "html",
        cache: false,
        success: function (data) {
            func_close_constructor(data)
        }
    });
    return false;
}

