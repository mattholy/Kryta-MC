$(document).ready(function () {
	$('#page02').hide();
	$('#page03').hide();
	$('#page04').hide();
	$('#page05').hide();

	$("#page01-next_page_btn").click(function(){
		$('#page02').show();
	});

	$("#page02-yes_btn").click(function(){
		$('#page03').show();
	});

	$("#page02-no_btn").click(function(){
		alert('你必须同意用户协议才能进行下一步')
	});

	$("#page03-verify").click(function(){
		$('#page04').show();
	});

	$("#page04-next_btn").click(function(){
		$('#page05').show();
	});
})