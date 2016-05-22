$(document).ready(function(){
	$("#closeAl").on("click",function(){
		$("#alert").fadeOut(500);
		$("#alert").remove();
	})
var ii="";
setInterval(function(){
var n=$('#forCrypt').val();
if (n.length>1){
if (ii!=n) {

$.getJSON($SCRIPT_ROOT + 'whatstep', {
crypt: $('#forCrypt').val(),
}, function(data) {
	
	$("#chart").append('<div class="jumbotron text-center"> <h2>'+data.result+'</h2></div>');

});


ii=n;
}


}
}, 2000)
$(function() {
$('a#crypt').bind('click', function() {
$("#chart").children().remove();
if (Number($("#step").val())<=25){
$("#stepInfo").html('Enter the ROTN <span style="font-size: 10px;">(from 0 to 25)</span>:');
$.getJSON($SCRIPT_ROOT + 'crypt', {
crypt: $('#forCrypt').val(),
step: $("#step").val()
}, function(data) {
$("#forDeCrypt").text(data.result);
var js=data.cou
for (var i=0;i<js.length;i++){
$("#chart").append('<div class="item text-center" style="background-color:'+js[i][2]+ ';height:'+js[i][1]+'px;"><p style="font-size:12px; margin-top:'+(js[i][1])+'px">'+'<span style="color:red">"'+js[i][0]+'"</span>'+': '+js[i][1]+'</p></div>')
}
});
}
else{
$("#stepInfo").html("<span style='color:red'>The ROTN must be a number from 0 to 25:</span>")
}
});
$('a#decrypt').bind('click', function() {
$("#chart").children().remove();
if (Number($("#step").val())<=25){
$("#stepInfo").html('Enter the ROTN <span style="font-size: 10px;">(from 0 to 25)</span>:');
$.getJSON($SCRIPT_ROOT + 'decrypt', {
crypt: $('#forCrypt').val(),
step: $("#step").val()
}, function(data) {
var js=data.cou
for (var i=0;i<js.length;i++){
$("#forDeCrypt").text(data.result);
$("#chart").append('<div class="item text-center" style="background-color:'+js[i][2]+ ';height:'+js[i][1]+'px;"><p style="font-size:12px; margin-top:'+(js[i][1])+'px">'+'<span style="color:red">"'+js[i][0]+'"</span>'+': '+js[i][1]+'</p></div>')
}

});
}
else{
$("#stepInfo").html("<span style='color:red'>The ROTN must be a number from 0 to 25:</span>")
}
});
});
})