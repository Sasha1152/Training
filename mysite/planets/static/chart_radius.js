google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawSeriesChart);

    function drawSeriesChart() {

      var data = google.visualization.arrayToDataTable([
        ['Name', 'Position', 'coordinate', 'Type',     'Radius, km'],
        ['Mercury', 1,          3,      'solid surface',  2440],
        ['Venus',   2,          3,      'solid surface',  6052],
        ['Earth',   3,          3,      'solid surface',  6371],
        ['Moon',    3,          2,      'solid surface',  1737],
        ['Mars',    4,          3,      'solid surface',  3390],
        ['Phobos',  4,          2,      'solid surface',  11],
        ['Deimos',  4,          1,      'solid surface',  6],
        ['Jupiter', 5,          3,      'gas surface',    69911],
        ['Saturn',  6,          3,      'gas surface',    58232],
        ['Uranus',  7,          3,      'gas surface',    25362],
        ['Neptune', 8,          3,      'gas surface',    24622],
        ['Pluto',   9,          3,      'solid surface',  1188],
      ]);

      var options = {
        title: 'Sizes of planets',
        bubble: {textStyle: {fontSize: 11}},
        chartArea: {left:30, top:30, bottom:30, right:100,
                    width:'10%', height:'10%', backgroundColor: 'grey'},
        backgroundColor: 'black',
      };

      var chart = new google.visualization.BubbleChart(document.getElementById('series_chart_div'));
      chart.draw(data, options);
    }