var A = {
	maxBarWidth : 1000,
	maxValue : 0,
	minValue : 9999,
	
	init : function(){
		
		A.maxBarWidth = $(".skill-bar").first().width();
		if(! A.maxBarWidth)
			console.log("error");
		A.createSkillsBarPercent();	
		
		$( window ).resize(function() {
			A.maxBarWidth = $(".skill-bar").first().width();
			A.createSkillsBarPercent();	
		});
		
		/* SVG */
		window.onload=function() {					
			
			var a = document.getElementById("ħobbies-svg");
			var svgDoc = a.contentDocument;
			
			if(svgDoc){
				$("#hobbies-legend li").each(function(){
				
					var legend = $(this);
					var tar = legend.attr("tar");
					var txt = legend.html();
					
					// Get one of the SVG items by ID;
					var svgItem = svgDoc.getElementById(tar+"_txt");
					if(svgItem){
						var tspan = svgItem.getElementsByTagName('tspan');
						if(tspan && tspan[0]){
							tspan[0].innerHTML = txt;
							tspan[0].style.fill = "#FFF";
						}
					}
					
				});
			}
		}
		
		/* ****************************
		 * 
		 * 	Contact
		 * 
		 * ***************************/
		 
		$(".show-mail-button div").on("click",function(){
			$(".mail-dialog").slideUp();
			$(".contact-form form").slideDown(); 
		});
		
		
	},
	
	createSkillsBarRelative : function(){		
		
		//Get max and min
		$(".skill").each( function(){
			var value = parseInt($(this).attr("value"));
			if( value > A.maxValue )
				A.maxValue = value;
			if( value < A.minValue )
				A.minValue = value;
		});
		
		
		var range = A.maxValue - A.minValue;
		$(".skill").each( function(){
			var value = $(this).attr("value");
			var bar = $(this).find(".bar");
			
			//calculate width according to max and min
			var percent = (value - A.minValue) / range;
		
			var bar_width = A.maxBarWidth /2 + A.maxBarWidth /2 * percent;
			
			bar.css("width",bar_width+"px");
		});
	},
	
	createSkillsBarPercent : function(){
		
		$(".skill").each( function(){
			var value = parseInt($(this).attr("value"));
			var bar = $(this).find(".bar");
			
			//calculate width according to max and min
			var percent = value/100;
			var bar_width = percent * A.maxBarWidth ;
			
			bar.css("width",bar_width+"px");
		});	
	},
}

$( document ).ready( A.init );
