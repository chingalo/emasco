$(document).ready(function(){
	//control for sinle message on administration navigation
	$("#adminMessageButtonContents").show();
	$("#senderinfoButttonDeatails").hide();
	;
	
    $("#adminMessageButton").click(function(){                
                $("#senderinfoButttonDeatails").hide();
                
                $("#adminMessageButtonContents").slideToggle();
                });            
    $("#senderinfoButtton").click(function(){ 
                $("#adminMessageButtonContents").hide();
                $("#senderinfoButttonDeatails").slideToggle();
                });  
	
});
