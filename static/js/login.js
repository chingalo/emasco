// logi validations

function loginValidate(){
	username = document.getElementById('adminstration_username').value;
	password = document.getElementById('adminstration_password').value;
	
	if (username == ""){
		alert('Fill username');
		return false;
		}
		
	if (password == ""){
		alert('Fill password');
		return false;
		}
		
	else{
		return true;
		}		
	
	}



function loginMoboValidate(){
	username = document.getElementById('adminstration_username_mobile').value;
	password = document.getElementById('adminstration_password_mobile').value;
	
	if (username == ""){
		alert('Fill username');
		return false;
		}
		
	if (password == ""){
		alert('Fill password');
		return false;
		}
		
	else{
		return true;
		}		
	
	}
