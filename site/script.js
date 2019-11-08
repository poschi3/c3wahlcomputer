function setCookie(name, value) {
    var date = new Date();
    date.setTime(date.getTime() + (60 * 1000));
    var expires = "; expires=" + date.toUTCString();
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) {
    document.cookie = name + '=; Max-Age=-99999999;';
}

function feel(feeling) {

    if(getCookie("marker") != null) {
        window.location.href = "https://show.feel.poschi.net/";
        return;
    }

    setCookie("marker", "PleaseBeNice");
    console.log(feeling);

    // HTTP-POST
    let request = new XMLHttpRequest();
    request.addEventListener('readystatechange', function (e) {
        if (this.readyState === 4) {
            window.location.href = "https://show.feel.poschi.net/";
        }
    });
    request.open('POST', '/api.php', true);
    request.setRequestHeader('Content-Type', 'application/json');
    let body = {
        "feeling": feeling
    }
    request.send(JSON.stringify(body));
}
