function marcoPolo(name) {
    if (name.toLowerCase() === "marco"){
        return "polo!";
    }

    return "Try Again!";
}

function respond(name, callback) {
    callback(name);
}
