$('#coll-back-form').submit(function() {
    alert('kk');
        var phone = $('#call_back_phone').val();
        var name = $('#call_back_name').val();
        $.ajax({
            type: "GET",
            url: "/call",
            data:{
                phone: phone,
                name: name
            },
            cache: false,
            dataType: "html",
            success: function(){
                document.getElementById('revers_commun').innerHTML = '<h4 style="padding: 0!important; margin: 0!important; color: white; font-size: 16pt; text-decoration: none">Отлично!</h4>' +
                    '<p style="padding-top: 5px!important; color: white; font-size: 12pt; text-decoration: none">Вскоре мы вам перезвоним</p>';
            },
            error: function (error) {
                alert(error)
            }
       });
    return false;
});