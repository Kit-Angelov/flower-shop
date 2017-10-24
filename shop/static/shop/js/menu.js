/**
 * Created by kit on 15.10.17.
 */
$(function() {
    var width = $('.menu_revers').css("width");
    var elem = $('#menu_revers');
    $("#menuvip").hover(
        function () {
            elem.css('left', '0');
        }, function () {
            elem.css('left', '-' + width);
        }
    );
    $("#menu_revers").hover(
        function () {
            elem.css('left', '0');
        }, function () {
            elem.css('left', '-' + width);
        }
    );
});