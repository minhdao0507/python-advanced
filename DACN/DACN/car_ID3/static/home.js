$(document).ready(function(){

    $("#predict").click(function(){
        var car = {
            "symboling" : Number($("#symboling").val()),
            "CarName" : $("#carname").val(),
            "fueltype" : $("#fueltype").val(),
            "aspiration": $("#aspiration").val(),
            "doornumber" : $("#doornumber").val(),
            "carbody" : $("#carbody").val(),
            "drivewheel" : $("#drivewheel").val(),
            "enginelocation" : $("#enginelocation").val(),
            "wheelbase" : Number($("#wheelbase").val()),
            "carlength" : Number($("#carlength").val()),
            "carwidth" : Number($("#carwidth").val()),
            "carheight" : Number($("#carheight").val()),
            "curbweight" : Number($("#curbweight").val()),
            "enginetype" : $("#enginetype").val(),
            "cylindernumber" : $("#cylindernumber").val(),
            "enginesize" : Number($("#enginesize").val()),
            "fuelsystem" : $("#fuelsystem").val(),
            "boreratio" : Number($("#boreratio").val()),
            "stroke" : Number($("#stroke").val()),
            "compressionratio" : Number($("#compressionratio").val()),
            "horsepower" : Number($("#horsepower").val()),
            "peakrpm" : Number($("#peakrpm").val()),
            "citympg" : Number($("#citympg").val()),
            "highwaympg" : Number($("#highwaympg").val()),
        }
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch("/car/",{
            method: 'POST',
            body: JSON.stringify({'car':car}),
            headers: { 
                "X-CSRFToken": csrftoken,
            }
        }).then(data=>data.text().then(text =>{
                console.log(text);
                document.getElementById("price_pred").value = text;
            }));
        console.log(car)
    });
});