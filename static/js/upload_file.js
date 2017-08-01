//upload_file.js
//文件上传
$(function() {
	$("#file_upload").uploadify({
		height: 30,
		removeCompleted : false,
		swf: '../static/flash/uploadify.swf',
		formData: {},
		uploader: '/',
		width: 80,
		'onUploadSuccess': function(file, data, response) {
			var result = jQuery.parseJSON(data);
			alert(result.msg);
		},
	});
});
