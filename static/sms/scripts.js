$(document).ready(function() {
	$(":checkbox").on('click', function() {
		$("h3").toggle();
	});
	$("#controls-toggle").on('click', function(event) {
		event.preventDefault();
		$("#controls").slideToggle();
	});
});
