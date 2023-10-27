const prog = document.querySelector("#prog");
const script = document.querySelector("#script");
const embed = document.querySelector("#embed");

const content = document.querySelector(".content-container");

let progLangs = ["Java", "C/C++", "Python"];
let scriptLangs = ["Perl", "Ruby", "Lua"];
let embedLangs = ["C/C++", "Rust", "Assembly"];

function defaultLoader() {
    content.innerHTML = "";
    progLangs.forEach(element => {
        content.innerHTML += `<p>${element}</p>`
    });
}

defaultLoader();

prog.addEventListener("click", function() {
    defaultLoader();
})

script.addEventListener("click", function() {
    content.innerHTML = "";
    scriptLangs.forEach(element => {
        content.innerHTML += `<p>${element}</p>`
    });
})

embed.addEventListener("click", function() {
    content.innerHTML = "";
    embedLangs.forEach(element => {
        content.innerHTML += `<p>${element}</p>`
    });
})
