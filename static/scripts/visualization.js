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
	Tweets.addEventListener('change',function () {
		if (Tweets.checked) viz.renderWithCypher(getNodes("Tweet"));
		else{}
    });

	Location.addEventListener('change',function () {
		if (Location.checked) viz.renderWithCypher(getNodes("Location"));
		else{}
	});

	Hashtag.addEventListener('change',function () {
		if (Hashtag.checked) viz.renderWithCypher(getNodes("Hashtag"));
		else{}
	});

	User.addEventListener('change',function () {
		if (User.checked) viz.renderWithCypher(getNodes("User"));
		else{}
	});

	Source.addEventListener('change',function () {
		if (Source.checked) viz.renderWithCypher(getNodes("Source"));
		else{}
	});
	Language.addEventListener('change',function () {
		if (Language.checked) viz.renderWithCypher(getNodes("Language"));
		else{}
	});
}

function relationshipsLabelsListener() {
	let HAS_TWEETED = document.getElementById("HAS_TWEETED");
	let IS_FROM = document.getElementById("IS_FROM");
	let HAS_MENTIONED = document.getElementById("HAS_MENTIONED");
	let HAS_TAG = document.getElementById("HAS_TAG");
	let TALKS = document.getElementById("TALKS");
	let VIA = document.getElementById("VIA");
	HAS_TWEETED.addEventListener('change',function () {
		if (HAS_TWEETED.checked) viz.renderWithCypher(getRelationShips("HAS_TWEETED"));
		else{}
    });

	IS_FROM.addEventListener('change',function () {
		if (IS_FROM.checked) viz.renderWithCypher(getRelationShips("IS_FROM"));
		else{}
	});

	HAS_TAG.addEventListener('change',function () {
		if (HAS_TAG.checked) viz.renderWithCypher(getRelationShips("HAS_TAG"));
		else{}
	});

	HAS_MENTIONED.addEventListener('change',function () {
		if (HAS_MENTIONED.checked) viz.renderWithCypher(getRelationShips("HAS_MENTIONED"));
		else{}
	});

	VIA.addEventListener('change',function () {
		if (VIA.checked) viz.renderWithCypher(getRelationShips("VIA"));
		else{}
	});
	TALKS.addEventListener('change',function () {
		if (TALKS.checked) viz.renderWithCypher(getRelationShips("TALKS"));
		else{}
	});

}

nodeLabelsListener();
relationshipsLabelsListener();