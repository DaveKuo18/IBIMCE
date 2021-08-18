$(document).ready(function(){
	var altura = $('.cuerpo').offset().top;

	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			$('.div-menu-peg').addClass('menu-peg-fixed');
		} else {
			$('.div-menu-peg').removeClass('menu-peg-fixed');
		}
	});
 
});