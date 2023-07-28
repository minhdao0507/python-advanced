$(document).ready(function(){

    $("button").click(function(){
        let user = {
            'username' : $("#username-login").val(),
            'password' : $("#pass-login").val()
        }
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch("/car/admin",{
            method: 'POST',
            body: JSON.stringify({'user':user}),
            headers: { 
                "X-CSRFToken": csrftoken,
            }
        }).then(response => window.location.assign("admin/home"));
        console.log("user: ", user);
    });
});