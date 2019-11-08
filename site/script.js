function feel(feeling) {
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
