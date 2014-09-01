$(document).ready(function(){
	//control for all links on administration navigation
	$("#servicesManagemntsLinks").hide();
	$("#messageMangementLinks").hide();
	$("#portfolioManagementLinks").hide();
	$("#accountManagementLinks").hide();
	$("#coreTeamManagementLinks").hide();
	
	$("#coreTeamManagement").click(function(){                
                $("#servicesManagemntsLinks").hide();
                $("#messageMangementLinks").hide();
                $("#portfolioManagementLinks").hide();
                $("#accountManagementLinks").hide();
                $("#coreTeamManagementLinks").slideToggle();
                });
    $("#accountManagement").click(function(){                
                $("#coreTeamManagementLinks").hide();
                $("#messageMangementLinks").hide();
                $("#portfolioManagementLinks").hide();
                $("#coreTeamManagementLinks").hide();
                $("#accountManagementLinks").slideToggle();
                });            
    $("#messageMangement").click(function(){                
                $("#portfolioManagementLinks").hide();
                $("#servicesManagemntsLinks").hide();
                $("#accountManagementLinks").hide();
                $("#coreTeamManagementLinks").hide();
                $("#messageMangementLinks").slideToggle();
              });
	$("#servicesManagemnts").click(function(){                
                $("#accountManagementLinks").hide();
                $("#messageMangementLinks").hide();
                $("#coreTeamManagementLinks").hide();
                $("#portfolioManagementLinks").hide();
                $("#servicesManagemntsLinks").slideToggle();
                }); 
    $("#portfolioManagement").click(function(){                
                $("#coreTeamManagementLinks").hide();
                $("#messageMangementLinks").hide();
                $("#accountManagementLinks").hide();
                $("#servicesManagemntsLinks").hide();
                $("#portfolioManagementLinks").slideToggle();
                });                     
	
	
	
});
