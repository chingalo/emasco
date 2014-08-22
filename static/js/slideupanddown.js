$(document).ready(function(){
		//for other devices
        $("#history_details").hide();        
        $("#experiance_details").hide();
        $("#specilazation_details").hide();
        
        //for mobiles
        $("#history_details_mobile").hide();        
        $("#experiance_details_mobile").hide();
        $("#specilazation_details_mobile").hide();
        
        //events for other devices
        $("#history").click(function(){
                $("#specilazation_details").hide();
                $("#experiance_details").hide();
                $("#history_details").slideToggle();
                });
        $("#experiance").click(function(){
                $("#specilazation_details").hide();
                $("#experiance_details").slideToggle();
                $("#history_details").hide();
                });

        $("#specilazation").click(function(){
                $("#specilazation_details").slideToggle();
                $("#experiance_details").hide();
                $("#history_details").hide();
                });
            
          //events for mobile phones      
         $("#history_mobile").click(function(){
                $("#specilazation_details_mobile").hide();
                $("#experiance_details_mobile").hide();
                $("#history_details_mobile").slideToggle();
                });
        $("#experiance_mobile").click(function(){
                $("#specilazation_details_mobile").hide();
                $("#experiance_details_mobile").slideToggle();
                $("#history_details_mobile").hide();
                });

        $("#specilazation_mobile").click(function(){
                $("#specilazation_details_mobile").slideToggle();
                $("#experiance_details_mobile").hide();
                $("#history_details_mobile").hide();
                });       

        });
       
