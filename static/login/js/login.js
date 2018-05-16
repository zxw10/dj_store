/**
 * Created by xlg on 2018/3/8.
 */
$(function () {
    $('input[name="userAccount"]').focus(function () {
        $('span').css('display','none');
        $('#errinfo').html('');
    })
    $('input[name="userPass"]').focus(function () {
        $('span').css('display','none');
        $('#errinfo').html('');
    })

})
function loginCheck(){
    username = $('input[name="userAccount"]').val();
    userPass = $('input[name="userPass"]').val();
    console.log(userPass.length)
    console.log(userPass.length>=6 && userPass.length<=12)
    if(username.match(/^[1][3-8][0-9]{9}$/) && userPass.match(/^\w{6,12}$/) ){
                console.log('为真');
        $.post('http://127.0.0.1:8000/dologin/',{userAccount:username,userPass:userPass},function (data,status) {
            console.log(data);
            console.log(status);
            var info;
            if(status=='success'){
                if(data['state']==200){
                    window.location.href = '/mine/';
                }else if(data['state']==201){
                    info = '密码不正确'
                }else if(data['state']==202){
                    info = '请输入正确的用户名'
                }
            }else{
                info = '请求失败'
            }
            $('#errinfo').html(info).css('display','block')

        })
    }else{
        console.log('为假');
        $('span').css('display','block');
    }
    return false
}
