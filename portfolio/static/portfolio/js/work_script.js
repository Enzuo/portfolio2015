function Work( e ){
	this.element = e;
	this.techs = new Array()
	
	this.getTechs();	
}
Work.prototype.getTechs = function(){
	list = this.element.find(".tech"); //return  jQuery collection
	self = this;
	
	list.each(function(){
		var tech_name = $( this ).attr("name");
		self.techs.push(tech_name);
	});
}
Work.prototype.hide = function(){
	this.element.hide();
}
Work.prototype.show = function(){
	this.element.show();
}

var WI = { //WI stands for WorkInteractions
	
	filters_menu : false,
	filter_list : new Array(),
	techs_nb : 1000,
	
	tags_filter_list : new Array(),
	
	work_list : new Array(),
	
	workview : false,
	
	ajaxTimer : false,
	
	init : function() {
			
		
		//If small screen < 520
		/*var w = $( window ).width();
		if( w <= 520 ){
			$(".thumbnail img").lazyload({
				skip_invisible : true,
			});	
		}*/
		/*
		var w = $( window ).width();
		if( w <= 520 ){
			WI.popWorkObjects( false );
			$(".thumbnail img").lazyload({
				skip_invisible : true,
			});	
		}
		else {
			//Call work objects pop
			WI.popWorkObjects( true );
		}*/
		
		/*************************************
		 * 
		 * SET UP Techs filters
		 * 
		 * **********************************/
		WI.populateWorkList();
		WI.techs_nb = $(".filter").length;
		$( ".filters-toggle" ).on({
			"click" : function( event ){
				event.preventDefault();
				if(WI.filters_menu){
					WI.rollUpFilterMenu();
				}
				else{
					WI.rollDownFilterMenu();
				}
					
			}
		});
		
		$( ".filters-reset" ).on("click",function(event){
			event.preventDefault();
			WI.resetFilters();
			WI.applyFilters();
		});
		
		$("#filters-list").on("click",".filter",function(){	
			WI.addFilter( $( this ) );
			WI.applyFilters();
		});
		
		
		/*************************************
		 * 
		 * SET UP Tags filters
		 * 
		 * **********************************/
		$("#tags-filters").on("click", "li", function(){
			var tag = $(this);
			var tag_id = tag.attr("data");
			tag.toggleClass("active");
			
			//Has changed so prepare to do AJAX
			WI.loadWorkList();
		});
	},
	
	
	setupWorkObjectsInteractions : function(){	
			
		//Add the listeners for .work objects	
		$( ".work" ).on({
			
			"mouseover" : function(){
				WI.displayDetails( $(this) );
			},
			
			"mouseout" : function(){
				WI.hideDetails( $(this) );
			},
		});
			

		//Set up work view
		WI.workview = $("#work-viewer");
		
		$(".work").on("click",function(){
			var content = $(this).find(".work-full").html();
			WI.displayWorkView( content );
		});
		
		$(".background").on("click",function(){
			WI.workview.hide();
		});
	},
	
	
	/***************************************
	 * 
	 * AJAX Loading functions
	 * 
	 * ************************************/
	 
	loadWorkList : function(){
		//set preloader
		$("#work-list-wrapper").html( '<div class="loader">loading...</div>' );

		var tagsFilters = $("#tags-filters li.active").map(function() { return $(this).attr("data")}).get().join("_");
		
		if(WI.ajaxTimer){
			clearTimeout(WI.ajaxTimer);
			WI.ajaxTimer = setTimeout(function(){
			
				WI.ajaxWorkList( tagsFilters );
			
			},1000);
		}
		else {
			console.log("DIRECT LOAD");
			WI.ajaxWorkList( tagsFilters );
			WI.ajaxTimer = true;
		}
	},
	
	ajaxWorkList : function( tagsFilters ){				
		
		$.ajax({
			url:"/worklist/", 
			data:{ tags:tagsFilters }, 
			dataType: "json",
			success: function(json){

				$("#work-list-wrapper").html(json['html']);			
				
				WI.populateWorkList();
				WI.applyFilters();
				WI.popWorkObjects( true );
				WI.setupWorkObjectsInteractions();
			},
			failure: function(){
				console.log("ajax error");
			}

		});
	},
	
	loadWorkDetails : function(){
	
	},
	
	
	/*********************************
	 * 
	 * Work objects functions
	 * 
	 * ******************************/
	
	displayWorkView : function( content ){
		WI.workview.find(".content").html(content);
		
		WI.workview.show();
	},
	
	displayDetails : function( e ){
		e.find( ".details" ).show();
	},
	
	hideDetails : function( e ){
		e.find( ".details" ).hide();
	},
	
	
	
	popObject : function( e ){
		e.not(':animated')
			.css({'opacity': 1 })
			.effect("scale", {
				origin:['middle','center'], 
				from:{width:e.width()/2,height:e.height()/2}, 
				percent: 100, 
				direction: 'both', 
			}, 700);	
	},
	
	popWorkObjects : function( animation ) {
		//If small screen < 520
		var w = $( window ).width();
		if( w <= 520 ){
			animation = false;
			$(".thumbnail img").lazyload({
				skip_invisible : true,
			});	
		}
		
		
		
		if( animation ){
			$( ".work" ).each(
				function(i){
					var e = $(this);
					setTimeout(function(){
						WI.popObject( e );
					},i*450);
				}	
			)
		}
		else
		{
			$( ".work" ).css({'opacity': 1 });
		}
	},
	
	
	/**********************************
	 * 
	 * Techs filter functions
	 * 
	 * ********************************/
	 
	rollDownFilterMenu : function() {
		$("#filters-bar").animate({
			right:"0px",
		},250, function(){ WI.filters_menu = true; });
	},
	
	rollUpFilterMenu : function() {
		var widthValue = $("#filters").width(); 
		widthValue = "-"+widthValue+"px"
		$("#filters-bar").animate({
			right:widthValue,
		},250, function(){ WI.filters_menu = false; });
	},
	
	addFilter : function( element ){
		console.log(element);
		
		//If nothing is filtered
		// --> Disable everything and put element as filter
		if(WI.filter_list.length == 0){
			$(".filter").addClass("disabled");
			element.removeClass("disabled");
			
			//get filter name
			var filter_name = element.attr("name");
			WI.filter_list.push( filter_name );
		}
		//Else we already have some elements
		// --> If element is not disabled then we disable it
		else if (!element.hasClass("disabled")){
			
			//remove Filter
			WI.removeFilter( element );
		}
		else{			
			
			//if all filter selected : RESET
			if(WI.filter_list.length +1 >= WI.techs_nb) {
				//RESET
				WI.resetFilters();
			}
			else
			{
				//Just append to the list
				element.removeClass("disabled");
				var filter_name = element.attr("name");
				WI.filter_list.push( filter_name );
			}
			
		}	
	},
	
	resetFilters : function(){
		$(".filter").removeClass("disabled");
		WI.filter_list.length = 0;
	},
	
	// Without forgetting to check that if last element got disabled then we reset
	removeFilter : function( element ){
		if( WI.filter_list.length == 1 ){
			$(".filter").removeClass("disabled");
			WI.filter_list.length = 0;
		}
		else{
			var filter_name = element.attr("name");
			if( (index = WI.filter_list.indexOf( filter_name )) >= 0){
				WI.filter_list.splice( index, 1 );
				element.addClass("disabled");
			}
		
		}
	},
	
	/**
	 * Apply Filters to all work objects, displaying or hiding them
	 * */
	applyFilters : function(){
		//choose for a work object to be displayed or not
		var arrayLength = WI.work_list.length;
		
		//If no filter then show everything
		if( WI.filter_list.length < 1){
			for (var i = 0; i < arrayLength; i++) {
				WI.work_list[i].show();
			}
		}
		else
		{
			for (var i = 0; i < arrayLength; i++) {
				
				var work = WI.work_list[i];
				
				if ( WI.isInFilters( work ) ){
					work.show();
				}
				else {
					work.hide();
				}
			}
		}
	},
	
	/**
	 * return true if the work is in the filter list and therefore should be displayed
	 * false if the work doesn't correspond to selected filters and so shouldn't be displayed
	 * */
	isInFilters : function( work ){
		//Search if any of the wanted tech is present
		var nb_tech = work.techs.length;
		for (var j = 0; j < nb_tech; j++){
			var tech = work.techs[j];
			
			var nb_filter =	WI.filter_list.length
			
			for(var k = 0; k < nb_filter; k++){
				var filter = WI.filter_list[k]
				if( tech == filter )
					return true;
			}
		}
		return false;
	},
	
	populateWorkList : function(){
		
		WI.work_list.length = 0;
		
		$(".work-wrapper").each(function(){
			var obj = new Work( $(this) );
			WI.work_list.push( obj );
		});
	},
	
}





$( document ).ready( function(){
	WI.init();
	WI.loadWorkList();
	
});
