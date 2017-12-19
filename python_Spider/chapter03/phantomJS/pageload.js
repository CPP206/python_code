var page = require('webpage').create();

page.open('http://www.cnblogs.com/miqi1992/', function(status){
	console.log("Status: "+status);
	if(status === "success"){
		page.render('qiye.png');
	}
	phantom.exit()
})