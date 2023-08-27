
window.addEventListener("scroll", () => {
    const header = document.querySelector(".header");
    if(window.scrollY > 0) {
        header.style.backgroundColor = "#212529";
        header.style.paddingTop = "0px";
    } else {
        header.style.backgroundColor = "";
        header.style.paddingTop = "36px";
    }
});