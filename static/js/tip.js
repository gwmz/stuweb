//更新tip框信息，其中tipName,tipTime,tipMessage都应由后台传递数值
function updateTip(){
	var tipName;
	var tipTime;
	var tipMessage;
	tipName="青蛙";
	tipTime="10秒钟前";
	tipMessage="被抓了吃了";
	document.getElementById("tipName1").firstChild.nodeValue=tipName;
	document.getElementById("tipTime1").firstChild.nodeValue=tipTime;
	document.getElementById("tipMessage1").firstChild.nodeValue=tipMessage;
	updateTip2();
}
function updateTip2(){
	var tipName;
	var tipTime;
	var tipMessage;
	tipName="土豆";
	tipTime="3分钟前";
	tipMessage="被炒了吃了";
	document.getElementById("tipName2").firstChild.nodeValue=tipName;
	document.getElementById("tipTime2").firstChild.nodeValue=tipTime;
	document.getElementById("tipMessage2").firstChild.nodeValue=tipMessage;
	updateTip3();
}
function updateTip3(){
	var tipName;
	var tipTime;
	var tipMessage;
	tipName="包子";
	tipTime="1小时前";
	tipMessage="被蒸了吃了";
	document.getElementById("tipName3").firstChild.nodeValue=tipName;
	document.getElementById("tipTime3").firstChild.nodeValue=tipTime;
	document.getElementById("tipMessage3").firstChild.nodeValue=tipMessage;
}

function mouseOver1(){
	backcolor=document.getElementById("tip1").style.backgroundColor;
	document.getElementById("tip1").style.backgroundColor="#f0ee2d";
}
function mouseOut1(){
	document.getElementById("tip1").style.backgroundColor=backcolor;
}
function mouseOver2(){
	backcolor=document.getElementById("tip2").style.backgroundColor;
	document.getElementById("tip2").style.backgroundColor="#f0ee2d";
}
function mouseOut2(){
	document.getElementById("tip2").style.backgroundColor=backcolor;
}
function mouseOver3(){
	backcolor=document.getElementById("tip3").style.backgroundColor;
	document.getElementById("tip3").style.backgroundColor="#f0ee2d";
}
function mouseOut3(){
	document.getElementById("tip3").style.backgroundColor=backcolor;
}