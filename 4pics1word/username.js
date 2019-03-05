function ajaxGetRequest(path, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}


function renderUsername(response){
    var usernameList = "";
    for(var data of JSON.parse(response)){
        usernameList = usernameList + data.message + "</br>";
    }
    document.getElementById("usernameList").innerHTML = chat;
}


function loadChat(){
    ajaxGetRequest("/username", renderUsername);
}


function sendUsername(){
    var usernameElement = document.getElementById("username");
    var username = usernameElement.value;
    usernameElement.value = "";
    var toSend = JSON.stringify({"username": username});
    ajaxPostRequest("/send", toSend, renderUsername);
}