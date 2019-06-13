String.prototype.trunc = String.prototype.trunc ||
      function(n){
          return (this.length > n) ? this.substr(0, n-1): this;
      };




function statsDrawer(data,chartId,chartLabel,charTitle,chartype,bdcolor,bgcolor,scaleType) {
    var received_labels = [];
    var received_scores = [];

    Object.keys(data).forEach(function (key) {
        Object.keys(data[key]).forEach(function (subKey) {
            let strdata = data[key][subKey]
            if (subKey === 'page') {received_labels.push(strdata)}
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
            label: [],
            borderColor: bdcolor,
            backgroundColor: bgcolor,
            data: received_scores
        }]
    },

        // Configuration options go here
        options: {
            legend: { display: false },
            circumference: 2*Math.PI,
            title: {
                display: true,
                text: charTitle
            },
            scales: {yAxes:scaleType}

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
            backgroundColor: ["rgb(0, 172, 238,0.69)", "rgba(249, 103, 122,0.69)",]
        }]
    },

        // Configuration options go here
        options: {
            circumference: Math.PI,
            rotation: -1*Math.PI,
            title: {
                display: true,
                text: 'Countries Validity'
            }
        }
    });
}

function topCountriesDrawer(data,chartId,chartTitle) {
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
        type: 'horizontalBar',

        // The data for our dataset
        data: {
        labels: received_labels,
        datasets: [{
            label: [],
            data: received_scores,
            backgroundColor: ["#00acee", "#f9677a","#3cba9f","#c45850","#e8c3b9"]
        }]
    },

        // Configuration options go here
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: chartTitle
            }
        }
    });
}