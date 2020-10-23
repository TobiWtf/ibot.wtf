// Written with love by tobi <3 //

var Download = "/files/download/";

async function files() { 
    var Files = await FILES();
    Files.forEach(file => {
        var element = document.createElement("a");
        element.innerText = file;
        element.href = Download + file;
        element.download = file;
        Break = document.createElement("br");
        Div = document.getElementById("Downloads");
        Div.appendChild(element);
        Div.appendChild(Break);
    });
}

files();