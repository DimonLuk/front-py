if($(".global").height() < $(window).height()){
	var tmp = $(".global").height()
	$(".global").height(Number($(window).height()))
	$("footer").css({"margin-top":$(".global").height()-tmp+16+"px"})
}
