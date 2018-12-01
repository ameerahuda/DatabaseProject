$(function(){

	$('#btnSignIn').click(function(){
		console.log("This is working so far");

		$.ajax({
			url: '/signIn',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
		console.log("This is working so far here");
	});

});