$(function() {
    $('#getRes').click(function() {
    	//waiting = 'Loading, please wait...',
    	//$("#loading").text(waiting);
    	//$("#result").text('');
        console.log('abcd')
        $.ajax({
            url: 'http://localhost:8999/predict',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response.prediction)
                //$("#result").text(response.prediction);
                for(var i=0;i<response.prediction.length;i++){
                    document.getElementById("resDiv").innerHTML += '<button type="button" class="btn btn-info preds" onclick="toggleClass(this)">'+response.prediction[i]+'</button>';
                }
                document.getElementById("resDiv").innerHTML += '<br><br><button type="button" class="btn btn-primary" onclick="finaltags()">Submit</button>'
            },
            error: function(error) {
                console.log(error);
            //    $("#loading").text('');
                $("#result").text('Something\'s phishy...');
            }
        });
    });
});

$(function() {
    $('#finalsub').click(function() {
        var larray = []
        var x = document.getElementsByClassName("preds");
        for(var i=0; i<x.length; i++) {
            larray.push(x[i].value)
        }
        console.log(larray)
    });
});

$(document).ready(function() {

            $("#getRes").click(function(){
               $("#partOne").toggle( 'slow', function(){
               });
               $("#partTwo").toggle( 'slow', function(){
               });
            });
         });

function toggleClass(button) {
    if(button.className === 'btn btn-info preds') {
        button.className = 'btn btn-success preds'
    }
    else{
        button.className = 'btn btn-info preds'
    }
}

function finaltags() {
    var larray = []
    var x = document.getElementsByClassName("preds");
    for(var i=0; i<x.length; i++) {
        if(x[i].className === 'btn btn-success preds') {
            larray.push(x[i].innerHTML)
        }
    }
    console.log(larray)
    finalReveal(larray);
}

function finalReveal(lr) {
    $(function(){
               $("#partTwo").toggle( 'slow', function(){
               });
               $("#partThree").toggle( 'slow', function(){
               });
    });

    document.getElementById("finalDiv").innerHTML += '<h4>Title</h4><p>' + document.getElementById("q_title").value + '</p>'
    document.getElementById("finalDiv").innerHTML += '<h4>Body</h4><p>' + document.getElementById("q_body").value + '</p>'
    document.getElementById("finalDiv").innerHTML += '<h4>Tags</h4><ul>'
    for(var i=0; i<lr.length; i++) {
        document.getElementById("finalDiv").innerHTML += '<li>' + lr[i] + '</li>'
    }
    document.getElementById("finalDiv").innerHTML += '</ul>'
}