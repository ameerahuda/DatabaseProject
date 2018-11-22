$(function(){
	// this will execute when the button for signup is pushed,
	// btnSignUp is the name of the button in the signup.html
	$('#btnSignUp').click(function(){
		console.log("This is working so far");
		// the url is the endpoint that is created in app.py
		// type is whatever you want to do, can be POST or GET
		$.ajax({
			url: '/signUp',
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