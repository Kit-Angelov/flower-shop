/**
 * Created by kit on 15.10.17.
 */
var h_hght = 100; // высота шапки
var h_mrg = 0; // отступ когда шапка уже не видна
var display = 'none';

$(function(){

    var elem = $('#navigate');
    var info = $('#info');
    var logo = $('#logo');
    var social = $('#social');
    var top = $(this).scrollTop();

    if(top > h_hght){
        elem.css('top', h_mrg);
}

$(window).scroll(function(){
    top = $(this).scrollTop();

    if (top+h_mrg < h_hght) {
        elem.css('top', (h_hght-top));
        elem.css('background-color', 'transparent');
        info.css('opacity', '1');
        info.css('transition', 'all ease 0.8s');
        logo.css('opacity', '1');
        logo.css('transition', 'all ease 0.8s');
        social.css('opacity', '1');
        social.css('transition', 'all ease 0.8s');
    } else {
        elem.css('top', h_mrg);
        elem.css('background-color', 'white');
        info.css('opacity', '0');
        info.css('transition', 'all ease 0.8s');
        logo.css('opacity', '0');
        logo.css('transition', 'all ease 0.8s');
        social.css('opacity', '0');
        social.css('transition', 'all ease 0.8s');
    }
});

});