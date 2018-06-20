function supportMusician() {
	var amount = Number($('input[name=amount]:checked').val());
	if(amount === 1 || amount === 2) {
		$('#support_confirmation_msg').html('Are you sure to support Yi ZHANG with ' + amount + '€?');
		$('#support_confirmation_modal').modal('show');
	} else {
		$('#support_nomoney_modal').modal('show');
	}
}

function supportSuccess() {
	$('#support_modal').modal('hide');
	$('#support_success_modal').modal('show');
}