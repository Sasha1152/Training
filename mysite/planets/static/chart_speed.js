google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = google.visualization.arrayToDataTable([
        ['Planet', 'Speed', { role: 'style' } ],
        ['Mercury', 10, 'color: gray'],
        ['Venus', 14, 'color: yellow'],
        ['Earth', 16, 'color: blue'],
        ['Mars', 22, 'color: red'],
        ['2050', 28, 'stroke-color: #871B47; stroke-opacity: 0.6; stroke-width: 8; fill-color: #BC5679; fill-opacity: 0.2']
      ]);

      var options = {
        title: 'Speed of planets',
        hAxis: {
          format: 'h:mm a',
          viewWindow: {
            min: [7, 30, 0],
            max: [17, 30, 0]
          }
        },
        vAxis: {
          title: 'Speed, km/s'
        }
      };

      var chart = new google.visualization.ColumnChart(
        document.getElementById('chart_div'));

      chart.draw(data, options);
    }