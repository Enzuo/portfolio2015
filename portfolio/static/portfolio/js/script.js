/*
var a = document.getElementById("gotowork");

a.addEventListener("click", function(event){
	event.preventDefault();
	
	gotowork_page();
	
});


var index = document.getElementById("index");

function gotowork_page(){
	index.className = "slide out";
	
	//Display the work elements
	setTimeout(function() { alert("displayed")}, 706);
	
	
}

function comebacktoindex(){
	index.className = "slide in reverse";
}
*/

/*
 * 
 * */
 
 
var SlideSwitcher = {
	
	slide1 : "index",
	slide2 : "work",
 
	init: function() {
		/* get the pages */
		SlideSwitcher.index = $("#index");
		SlideSwitcher.work = $("#work");
		
		/* assign links*/
		a = $("a[href='work']")
		a.bind("click", SlideSwitcher.gotoWork);
		
		a = $("a[href^='index']")
		a.bind("click", SlideSwitcher.gotoIndex);
		
		/* hover behavior*/
		$( ".work" ).hover(
			function() {
				$( this ).find( ".details" ).show();
			}, function() {
				$( this ).find( ".details" ).hide();
			}
		);
		
		/*filters*/
		$( ".toggle" ).click(function(e){
			e.preventDefault();
			$( "#filters" ).css({animate:".5",right:"0px"});
		});
		
		/*scroll*/
		$("#work-list").tinyscrollbar();
		
	},
	
	gotoIndex: function(event) {
		event.preventDefault();
		SlideSwitcher.index.removeClass().addClass("slide in reverse");
		
	},
	
	gotoWork: function(event) {
		event.preventDefault();
		SlideSwitcher.index.removeClass().addClass("slide out");
		
		setTimeout(function(){ 
			SlideSwitcher.popWorkObjects();
		},350);
		
		//history.pushState(stateObj, "page 2", "/work");
		
	},
	
	popWorkObjects: function() {
		$( ".work" ).each(function(i){
			var e = $(this);
			setTimeout(function(){ 
				e.not(':animated')
					.css({'opacity': 1 })
					.effect("scale", 
						{
							origin:['middle','center'], 
							from:{width:e.width()/2,height:e.height()/2}, 
							percent: 100, 
							direction: 'both', 
						}, 700);			
			},i*250);
		});
	}
 
 
};
 
$( document ).ready( SlideSwitcher.init );
