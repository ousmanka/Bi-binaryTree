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


function renderUsernames(response){
    var username = "";
    for(var data of JSON.parse(response)){
        username = username + data.username + "</br>";
    }
    document.getElementById("username").innerHTML = username;
}


function loadUsernames(){
    ajaxGetRequest("/username", renderUsernames);
}


function sendUsername(){
    var usernameElement = document.getElementById("username");
    var username = usernameElement.value;
    usernameElement.value = "";
    var toSend = JSON.stringify({"username": username});