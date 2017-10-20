// /**
//  * Created by kit on 19.10.17.
//  */
// function  get_package_list() {
//     alert("OK");
//     $.ajax({
//         type: "GET",
//         url: "/get_package_list",
//         data: {},
//         dataType: "html",
//         cache: false,
//         success: function (data) {
//             alert("OK");
//             var select = $('#select_package');
//             var listitems ={};
//             $.each(select, function(data){
//                 listitems += '<option id=' + data.elem_id + '>' +data.name + '</option>';
//             });
//              {
//
//             }
//         select.append(listitems);
//         })
//     return false
//     }