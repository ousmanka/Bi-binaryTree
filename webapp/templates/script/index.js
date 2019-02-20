function doFirst() {
    var button = document.getElementById('button');
    var button2 = document.getElementById('button2');
    button.addEventListener('click', getName, false);
    button2.addEventListener('click', getName, false);

}

function getName() {
    var user = document.getElementById('user').value;
    console.log(user);
}

function TriggeredKey(e) {
    var keycode;
    if (window.event) keycode = window.event.keyCode;
    if (window.event.keyCode == 13) return false;
}

window.addEventListener('load', doFirst, false);
