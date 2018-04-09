window.onload = function () {
var chart = new CanvasJS.Chart("chartRadius", {
	animationEnabled: true,
	zoomEnabled: true,
	theme: "dark1",
	title:{
		text: "Employment in Agriculture vs Agri-Land and Population"
	},
	axisX: {
		title:" ",
		suffix: " ",
		minimum: 0,
		maximum: 10,
		gridThickness: 1
	},
	axisY:{
		title: " ",
		suffix: " ",
		maximum: 2
	},
	data: [{
		type: "bubble",
		toolTipContent: "<b>{name}</b><br/>Employment: {x}% <br/> Agri-Land: {y}mn sq. km<br/> Radius: {z}km",
		dataPoints: [
			{ x: 1, y: 1, z:1347, name:"China" },
			{ x: 2, y: 1, z:21.49, name:"Australia" },
			{ x: 3, y: 1, z:304.09, name:"US" },
			{ x: 4, y: 1, z:2.64, name:"Brazil" },
			{ x: 5, y: 1, z:141.95, name:"Russia" },
			{ x: 6, y: 1, z:1190.86, name:"India" },
			{ x: 7, y: 1, z:26.16, name:"Saudi Arabia" },
			{ x: 8, y: 1, z:39.71, name:"Argentina" },
			{ x: 9, y: 1, z:48.79, name:"SA" },
		]
	}]
});
chart.render();

}
