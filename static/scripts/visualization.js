    function showViz() {
        var vizBlock = document.getElementById("mainDiv");
        if (vizBlock.style.display === "none") {
            vizBlock.style.display = "block";
        }
    }

    function drawAll(viz){
		viz.render();
	}


	function initVizFrame() {
    		var config = {
		    container_id:"mainDiv",
			server_url:"bolt://localhost:11001",
			server_user:"neo4j",
			server_password:"123456",
				initial_cypher: "MATCH (a)-[r]-(b) return a,r,b",
		};
    		return new NeoVis.default(config);
    }
	/*
	function getNodeLabels(Viz) {
        var nodeLabels = Viz.renderWithCypher("CALL db.labels()");
        if(nodeLabels == undefined) {
        	console.log("No record exists");
		}else {
        	nodeLabels = nodeLabels.slice(1);
		nodeLabels.forEach(function (e) {
			var json = JSON.stringify(e);
			console.log(json.length);

        });
        //return nodeLabels;
		}
    }
	*/

	function stabilize(viz) {
	    viz.stabilize();
    }


    window.addEventListener('load',function () {
		var viz = initVizFrame();
		var visualize = document.getElementById('Visualize');
		var stop = document.getElementById('Stop');

		visualize.addEventListener('click', function () {
			showViz();
			drawAll(viz);
		});

		stop.addEventListener('click',function () {
			stabilize(viz);
		})


    });
