$(document).ready(function(){
	//control for all activites iin single portfolio in mobile
	$("#portfolio_description_details_mobile").hide();
	$("#portfolio_client_details_mobile").hide();
	$("#portfolio_gallery_details_mobile").hide();
	
	$("#portfolio_description_mobile").click(function(){                
                $("#portfolio_gallery_details_mobile").hide();
                $("#portfolio_client_details_mobile").hide();
                $("#portfolio_description_details_mobile").slideToggle();
                });
    $("#portfolio_client_mobile").click(function(){                
                $("#portfolio_description_details_mobile").hide();
                $("#portfolio_gallery_details_mobile").hide();
                $("#portfolio_client_details_mobile").slideToggle();
                });
    $("#portfolio_gallery_mobile").click(function(){                
                $("#portfolio_description_details_mobile").hide();
                $("#portfolio_client_details_mobile").hide();
                $("#portfolio_gallery_details_mobile").slideToggle();
                });                     
	
	
	//for other devices
	$("#portfolio_description_details").hide();
	$("#portfolio_client_details").hide();	
	
	$("#portfolio_description").click(function(){ 
                $("#portfolio_client_details").hide();
                $("#portfolio_description_details").slideToggle();
                });
    $("#portfolio_client").click(function(){                
                $("#portfolio_description_details").hide();
                $("#portfolio_client_details").slideToggle();
                });
	
});
