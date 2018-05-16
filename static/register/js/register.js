$(function(){
    $('#accunt').blur(function(){
        var username = $(this).val();
        $.getJSON('http://127.0.0.1:8001/checkUsername/',{'name':username},function (data) {
            if(data['state']==1){
                $('#checkerr').css('display','block')
            }
        })
    }).focus(function(){
        $('#checkerr').css('display','none')
    })
});

function check(){
    var pass1 = $('#pass').val();
    var pass2 = $('#passwd').val();
    if(pass1 != pass2){
        $('#passwderr').css('display','block')
        return false

    }
}