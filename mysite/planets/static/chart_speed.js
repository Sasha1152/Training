window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "dark1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Top Oil Reserves"
	},
	axisY: {
		title: "Reserves(MMbbl)"
	},
	data: [{
		type: "column",
		showInLegend: true,
		legendMarkerColor: "grey",
		legendText: "MMbbl = one million barrels",
		dataPoints: [
			{ y: 300878, label: "Mercury" },
			{ y: 266455,  label: "Venus" },
			{ y: 169709,  label: "Earth" },
			{ y: 158400,  label: "Mars" },
			{ y: 142503,  label: "Iraq" },
			{ y: 101500, label: "Kuwait" },
			{ y: 97800,  label: "UAE" },
			{ y: 80000,  label: "Russia" }
		]
	}]
});
chart.render();

}