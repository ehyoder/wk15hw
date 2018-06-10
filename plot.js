var pieData = [{
  values: sampleData[0]['sample_values'].slice(0, 10),
  labels: sampleData[0]['otu_ids'].slice(0, 10),
  hovertext: labels.slice(0, 10),
  hoverinfo: 'hovertext',
  type: 'pie'
}];
var pieLayout = {
  margin: { t: 0, l: 0 }
};
var PIE = document.getElementById('pie');
Plotly.plot(PIE, pieData, pieLayout);
};
init();