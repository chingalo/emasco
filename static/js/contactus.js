$(document).ready(function(){
		
        $("#companyinfo").hide();        
        $("#contactmessage").hide();
       
        $("#companyinfobutton").click(function(){                
                $("#contactmessage").hide();
                $("#companyinfo").slideToggle();
                });
        $("#contactmessagebutton").click(function(){
                $("#companyinfo").hide();
                $("#contactmessage").slideToggle();                
                });

       

        });
       
