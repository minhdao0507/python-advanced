$(document).ready(function(){

    $("#train").click(function(){
        let date = {'date': $("#date").val()};
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch("/car/admin/home",{
            method: 'POST',
            body: JSON.stringify({'date':date}),
            headers: { 
                "X-CSRFToken": csrftoken,
            }
        }).then(data=>data.text().then(text =>{
            console.log(text);
            document.getElementById("score").value = text;
            $("#img").show();
        }));
        //console.log(date);
        //$("#img").show();
    });
});