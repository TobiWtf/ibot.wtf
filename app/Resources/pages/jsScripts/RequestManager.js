// Written with love by tobi <3 //

async function GET(url) {
    let response = await fetch(url);
    let data = await response.json();
    return data;
}

async function FILES() {
    return await GET("/files?List=true");
}