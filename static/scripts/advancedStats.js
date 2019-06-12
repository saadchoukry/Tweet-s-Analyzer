String.prototype.trunc = String.prototype.trunc ||
      function(n){
          return (this.length > n) ? this.substr(0, n-1): this;
      };




function statsDrawer(data,chartId,chartLabel,chartype,bdcolor,bgcolor) {
    var received_labels = [];
    var received_scores = [];

    Object.keys(data).forEach(function (key) {
        Object.keys(data[key]).forEach(function (subKey) {
            let strdata = data[key][subKey]
            if (subKey === 'page') {received_labels.push(strdata.trunc(25))}
            else {
                received_scores.push(data[key][subKey]);
            }
        });
    });
    console.log(received_scores);
    var ctx = document.getElementById(chartId).getContext('2d');
    var chart = new Chart(ctx, {

        // The type of chart we want to create
        type: chartype,

        // The data for our dataset
        data: {
        labels: received_labels,
        datasets: [{
            label: chartLabel,
            borderColor: bdcolor,
            backgroundColor: bgcolor,
            data: received_scores
        }]
    },

        // Configuration options go here
        options: {
            circumference: Math.PI,
            rotation: -1*Math.PI
        }
    });
}


function statsDrawerMapping(data,chartId,chartLabel) {
    var received_labels = [];
    var received_scores = [];

    Object.keys(data).forEach(function (key) {
        received_labels.push(key);
        received_scores.push(data[key]);
    });
    console.log(received_scores);

    console.log(received_labels);

    console.log(received_scores);
    var ctx = document.getElementById(chartId).getContext('2d');
    var chart = new Chart(ctx, {

        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
        labels: received_labels,
        datasets: [{
            label: chartLabel,
            data: received_scores,
            backgroundColor: ["#00acee", "#f9677a",]
        }]
    },

        // Configuration options go here
        options: {
            circumference: Math.PI,
            rotation: -1*Math.PI
        }
    });
}