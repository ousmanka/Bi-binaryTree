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


function renderGuesses(response){
    var chat = "";
    for(var data of JSON.parse(response)){
        chat = chat + data.message + "</br>";
    }
    document.getElementById("guessList").innerHTML = chat;
}


function loadGuesses(){
    ajaxGetRequest("/guess", renderGuesses);
}


function sendGuesses(){
    var guessElement = document.getElementById("guess");
    var guess = guessElement.value;
    guessElement.value = "";
    var toSend = JSON.stringify({"guess": guess});
    ajaxPostRequest("/send", toSend, renderGuesses);
}