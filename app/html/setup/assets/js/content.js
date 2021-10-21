$(document).ready(function () {
	$.get('setup/static/content/zh-cn.json', function(data,state) {
		for (pos in data['content']) {
			$("#" + pos).html(data['content'][pos])
		};
		for (pos in data['placeholder']) {
			$("#" + pos).attr( "placeholder", data['placeholder'][pos])
		};
	});
	
})