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
			server_url:"bolt://localhost:11008",
			server_user:"neo4j",
			server_password:"123456",
			initial_cypher: "MATCH (a)-[r]-(b) return a,r,b",
		};
		return new NeoVis.default(config);
}

function stabilize(viz) {
	viz.stabilize();
}

var viz;
window.addEventListener('load',function () {
	viz = initVizFrame();
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


function showNodeLabels() {
	var nodeLabelLink = document.getElementById("nodeLabels");
	nodeLabelLink.addEventListener('click',function () {
        var nodeLabels = document.getElementsByClassName("nodeLabels");
        var relLabels = document.getElementsByClassName("relLabels");
		for (let i=0;i<nodeLabels.length;i+=1) {
            nodeLabels[i].style.display = 'block';
        }

        for (let i=0;i<relLabels.length;i+=1) {
            relLabels[i].style.display = 'none';
        }
    });
}

function showRelationshipsLabels() {
	var relLabelLink = document.getElementById("relLabels");
	relLabelLink.addEventListener('click',function () {
        var nodeLabels = document.getElementsByClassName("nodeLabels");
        var relLabels = document.getElementsByClassName("relLabels");
		for (let i=0;i<nodeLabels.length;i+=1) {
            nodeLabels[i].style.display = 'none';
        }

        for (let i=0;i<relLabels.length;i+=1) {
            relLabels[i].style.display = 'block';
        }
    });
}

showNodeLabels();
showRelationshipsLabels();


function getNodes(nodeLabel) {
	let cypherStatement = "MATCH (N:"+nodeLabel+") RETURN N";
	console.log(cypherStatement);
	return cypherStatement
}

function getRelationShips(relationShipLabel) {
    let cypherStatement = "MATCH (a)-[R:" + relationShipLabel + "]-(b) RETURN R,a,b;";
    console.log(cypherStatement);
    return cypherStatement;
}

function nodeLabelsListener(){
	let Tweets = document.getElementById("Tweet");
	let Location = document.getElementById("Location");
	let User = document.getElementById("User");
	let Hashtag = document.getElementById("Hashtag");
	let Language = document.getElementById("Language");
	let Source = document.getElementById("Source");
	let AllNodes = document.getElementById("allNodes");
	Tweets.addEventListener('click',function () {
		viz.renderWithCypher(getNodes("Tweet"));
    });

	Location.addEventListener('click',function () {
		viz.renderWithCypher(getNodes("Location"));
	});

	Hashtag.addEventListener('click',function () {
		viz.renderWithCypher(getNodes("Hashtag"));
	});

	User.addEventListener('click',function () {
		viz.renderWithCypher(getNodes("User"));
	});

	Source.addEventListener('click',function () {
		viz.renderWithCypher(getNodes("Source"));
	});

	Language.addEventListener('click',function () {
		viz.renderWithCypher(getNodes("Language"));
	});

	AllNodes.addEventListener('click',function () {
		viz.renderWithCypher("MATCH (N) RETURN N");
    });
}

function relationshipsLabelsListener() {
	let HAS_TWEETED = document.getElementById("HAS_TWEETED");
	let IS_FROM = document.getElementById("IS_FROM");
	let HAS_MENTIONED = document.getElementById("HAS_MENTIONED");
	let HAS_TAG = document.getElementById("HAS_TAG");
	let TALKS = document.getElementById("TALKS");
	let VIA = document.getElementById("VIA");
	let HAS_RETWEETED = document.getElementById("HAS_RETWEETED");
	let IS_POSTED_FROM = document.getElementById("IS_POSTED_FROM");
	let AllRelations = document.getElementById("allRel");

	HAS_TWEETED.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("HAS_TWEETED"));
    });

	IS_FROM.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("IS_FROM"));
	});

	HAS_TAG.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("HAS_TAG"));
	});

	HAS_MENTIONED.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("HAS_MENTIONED"));
	});

	VIA.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("VIA"));
	});
	TALKS.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("TALKS"));
	});

	HAS_RETWEETED.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("HAS_RETWEETED"));
	});

	AllRelations.addEventListener('click',function () {
		viz.renderWithCypher("MATCH (N)-[R]->(M) RETURN N,R,M");
    });

	IS_POSTED_FROM.addEventListener('click',function () {
		viz.renderWithCypher(getRelationShips("IS_POSTED_FROM"));
    });


}

nodeLabelsListener();
relationshipsLabelsListener();

