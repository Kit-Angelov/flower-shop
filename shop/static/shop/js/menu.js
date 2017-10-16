/**
 * Created by kit on 15.10.17.
 */
$(function() {
    var elem = $('#menu_revers');
    $("#menuvip").hover(
        function () {
            elem.css('left', '0');
        }, function () {
            elem.css('left', '-200px');
        }
    );
    $("#menu_revers").hover(
        function () {
            elem.css('left', '0');
        }, function () {
            elem.css('left', '-200px');
        }
    );
});