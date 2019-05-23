 function clearBox(elementID) {
        document.getElementById(elementID).innerHTML = "";
        }

function getByScreenName() {

    clearBox("formDiv");
    var count=document.createElement("input");
    var since=document.createElement("input");
    var screen=document.createElement("input");
    var submit=document.createElement("button");
    count.setAttribute("type","number");
    count.setAttribute("class","form-control");
    count.setAttribute("id","count");
    count.setAttribute("name","count");
    since.setAttribute("type","Date");
    since.setAttribute("class","form-control");
    since.setAttribute("id","since");
    since.setAttribute("name","since");
    screen.setAttribute("type","text");
    screen.setAttribute("class","form-control");
    screen.setAttribute("id","screen");
    screen.setAttribute("name","screen");
    submit.setAttribute("class","btn btn-primary");
    submit.setAttribute("type","submit")
    submit.innerText="Search";
    var countLabel=document.createElement("label");
    countLabel.setAttribute("for","count");
    countLabel.innerText="Tweets limit:";
    var screenLabel=document.createElement("label");
    screenLabel.setAttribute("for","screen");
    screenLabel.innerText="Screen name:";
    var sinceLabel=document.createElement("label");
    sinceLabel.setAttribute("for","since");
    sinceLabel.innerText="Since:";


    var form=document.getElementById("formDiv");

    form.appendChild(document.createElement("br"));
    form.appendChild(screenLabel);
    form.appendChild(screen);
    form.appendChild(document.createElement("br"));
    form.appendChild(sinceLabel);
    form.appendChild(since);
    form.appendChild(document.createElement("br"));
    form.appendChild(countLabel);
    form.appendChild(count);

    form.appendChild(document.createElement("br"));
    form.appendChild(submit);
    form.appendChild(document.createElement("br"));
}


var selection = document.getElementById("offstr_type");

function getByHashTag() {
    clearBox("formDiv");
    var count=document.createElement("input");
    var since=document.createElement("input");
    var tag=document.createElement("input");
    var submit=document.createElement("button");
    count.setAttribute("type","number");
    count.setAttribute("class","form-control");
    count.setAttribute("id","count");
    count.setAttribute("name","count");
    since.setAttribute("type","Date");
    since.setAttribute("class","form-control");
    since.setAttribute("id","since");
    since.setAttribute("name","since");
    tag.setAttribute("type","text");
    tag.setAttribute("class","form-control");
    tag.setAttribute("id","tag");
    tag.setAttribute("name","tag");
    submit.setAttribute("class","btn btn-primary");
    submit.setAttribute("type","submit")
    submit.innerText="Search";
    var countLabel=document.createElement("label");
    countLabel.setAttribute("for","count");
    countLabel.innerText="Tweets limit:";
    var tagLabel=document.createElement("label");
    tagLabel.setAttribute("for","tag");
    tagLabel.innerText="Hashtag:";
    var sinceLabel=document.createElement("label");
    sinceLabel.setAttribute("for","since");
    sinceLabel.innerText="Since:";


    var form=document.getElementById("formDiv");

    form.appendChild(document.createElement("br"));
    form.appendChild(tagLabel);
    form.appendChild(tag);
    form.appendChild(document.createElement("br"));
    form.appendChild(sinceLabel);
    form.appendChild(since);
    form.appendChild(document.createElement("br"));
    form.appendChild(countLabel);
    form.appendChild(count);

    form.appendChild(document.createElement("br"));
    form.appendChild(submit);
    form.appendChild(document.createElement("br"));
}

function getByKeyWords() {
    clearBox("formDiv");
    var count=document.createElement("input");
    var since=document.createElement("input");
    var keywords=document.createElement("input");
    var submit=document.createElement("button");
    count.setAttribute("type","number");
    count.setAttribute("class","form-control");
    count.setAttribute("id","count");
    count.setAttribute("name","count");
    since.setAttribute("type","Date");
    since.setAttribute("class","form-control");
    since.setAttribute("id","since");
    since.setAttribute("name","since");
    keywords.setAttribute("type","text");
    keywords.setAttribute("class","form-control");
    keywords.setAttribute("id","keywords1");
    keywords.setAttribute("name","keywords1");
    submit.setAttribute("class","btn btn-primary");
    submit.setAttribute("type","submit")
    submit.innerText="Search";
    var countLabel=document.createElement("label");
    countLabel.setAttribute("for","count");
    countLabel.innerText="Tweets limit:";
    var keyLabel=document.createElement("label");
    keyLabel.setAttribute("for","keywords1");
    keyLabel.innerText="Keywords:";
    var sinceLabel=document.createElement("label");
    sinceLabel.setAttribute("for","since");
    sinceLabel.innerText="Since:";


    var form=document.getElementById("formDiv");
    form.appendChild(document.createElement("br"));
    form.appendChild(keyLabel);
    form.appendChild(keywords);
    form.appendChild(document.createElement("br"));
    form.appendChild(sinceLabel);
    form.appendChild(since);
    form.appendChild(document.createElement("br"));
    form.appendChild(countLabel);
    form.appendChild(count);

    form.appendChild(document.createElement("br"));
    form.appendChild(submit);
    form.appendChild(document.createElement("br"));
}