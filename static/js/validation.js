




//contact us message validation   
function sendContactMessageMobile(){
	fullname = document.getElementById('contact_full_name_mobile').value;
	email = document.getElementById('contact_email_mobile').value;
	mobilenumber = document.getElementById('contact_mobile_number_mobile').value;
	occupation = document.getElementById('occupation_mobile').value;
	subject = document.getElementById('contact_subject_mobile').value;
	message = document.getElementById('conatct_message_mobile').value;
	
	
	if (fullname == ""){
		alert("fill your full name");
		document.getElementById('contact_full_name_mobile').focus();
		return false;
		}
		
	if (email == "" && mobilenumber == ""){
		alert("You must fill e-mail or mobile number_mobile");		
		return false;
		}	
		//validate e-mail
	if (mobilenumber == ""){
		var atpos = email.indexOf('@')
		var atdot = email.lastIndexOf('.');
		if(atpos < 1 || atdot < atpos+2 || atdot+2 >= email.length){
			alert('Incorrect e-mail');
			document.getElementById('contact_email_mobile').focus();
			return false;
			}
		}
	if (occupation == ""){
		alert("fill your Occupation");
		return false;
		}
			
	if (subject == ""){
		alert("fill subject for your message");
		return false;
		}
	
	if (message == ""){
		alert("fill your message");
		return false;
		}	
		
	
	}


function sendContactMessage(){
	fullname = document.getElementById('contact_full_name').value;
	email = document.getElementById('contact_email').value;
	mobilenumber = document.getElementById('contact_mobile_number').value;	
	occupation = document.getElementById('occupation').value;	
	subject = document.getElementById('contact_subject').value;
	message = document.getElementById('conatct_message').value;
	
	
	if (fullname == ""){
		alert("fill your full name");
		document.getElementById('contact_full_name').focus();
		return false;
		}
		
	if (email == "" && mobilenumber == ""){
		alert("You must fill e-mail or mobile number");		
		return false;
		}	
		//validate e-mail
	if (mobilenumber == ""){
		var atpos = email.indexOf('@')
		var atdot = email.lastIndexOf('.');
		if(atpos < 1 || atdot < atpos+2 || atdot+2 >= email.length){
			alert('Incorrect e-mail');
			document.getElementById('contact_email').focus();
			return false;
			}
		}
			
	if (occupation == ""){
		alert("fill your Occupation");
		return false;
		}
		
	if (subject == ""){
		alert("fill subject for your message");
		return false;
		}
	
	if (message == ""){
		alert("fill your message");
		return false;
		}	
		
	
	}
