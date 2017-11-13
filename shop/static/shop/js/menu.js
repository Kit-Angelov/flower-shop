/**
 * Created by kit on 15.10.17.
 */
function menu() {
    var width = $('.menu_revers').css("width");
    var elem = $('#menu_revers');
    var close_elem = $('#menu-revers-close');
    elem.css('left', '0');
    // elem.css('left', '-' + width);
    close_elem.click(
        function () {
            elem.css('left', '-' + width);
        }
    );
}