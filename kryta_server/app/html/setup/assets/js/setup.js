$(document).ready(function () {
	$('#page02').hide();
	$('#page03').hide();
	$('#page04').hide();
	$('#page05').hide();

	$("#page01-next_page_btn").click(function(){
		$.ajax({
			url:"/setup/begin",
			method:'post',
			contentType: "application/json; charset=utf-8",
			success:function(result){
				console.log(result);
				$("#page01-next_page_btn").removeClass("fa-spin fa-spinner");
				$("#page01-next_page_btn").addClass("fa-check");
				$("#page01-next_page_btn").hide();
				$('#page02').show();
				document.getElementById("page01to02").click();
			},
			beforeSend:function(){
				$("#page01-next_page_btn").removeClass("fa-angle-right")
				$("#page01-next_page_btn").addClass("fa-spin fa-spinner")
			}
		});
	});

	$("#page02-yes_btn").click(function(){
		$.ajax({
			url:"/setup/eula",
			method:'post',
			// data:JSON.stringify({
			// 	name:'123'
			// }),
			contentType: "application/json; charset=utf-8",
			success:function(result){
				console.log(result);
				$("#page02-no_btn").html('已签署')
				$("#page02-yes_btn").hide();
				$('#page03').show();
				document.getElementById("page02to03").click();
			},
			beforeSend:function(){
				$("#page02-yes_btn").html('请稍后...')
			}
		});
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