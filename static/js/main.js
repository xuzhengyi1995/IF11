function supportMusician() {
	var amount = Number($('input[name=amount]:checked').val());
	if(amount === 1 || amount === 2) {
		$('#support_confirmation_msg').html('Are you sure to support Yifan WU with ' + amount + '€?');
		$('#support_confirmation_modal').modal('show');
	} else {
		$('#support_nomoney_modal').modal('show');
	}
}

function supportSuccess() {
	$('#support_modal').modal('hide');
	$('#support_success_modal').modal('show');
}
window.onload=function(){
	document.getElementById("music_file").onchange=function(e){
		file = e.target.files[0];
		src = window.createObjectURL&&window.createObjectURL(file)||window.URL&&window.URL.createObjectURL(file)||window.webkitURL && window.webkitURL.createObjectURL(file);
		console.log(file);
		console.log(src);
		audio = document.getElementById("audio_preview");
		audio.style.display='block';
	  audio.src=src;
	}
}
function getCookie(c_name){
	if (document.cookie.length>0){
	  c_start=document.cookie.indexOf(c_name + "=");
	  if (c_start!=-1){
	    c_start=c_start + c_name.length+1 ;
	    c_end=document.cookie.indexOf(";",c_start);
	    if (c_end==-1) c_end=document.cookie.length;
	    return unescape(document.cookie.substring(c_start,c_end));
	  }
	}
	return "";
}

function addMusic() {
	var form = new FormData(document.getElementById("up_form"));
	$.ajax({
		url:"/uploadmusic",
		type:"post",
		data:form,
		processData:false,
		contentType:false,
		success:function(data){
				console.log(data);
				alert(data);
		},
		error:function(e){
				alert("Error!");
		}
	});
}
