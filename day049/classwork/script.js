const share = document.getElementById("arrow");
const script = document.getElementById("scripted");

share.addEventListener("click", () => {
    if (script.style.display === "flex") {
        script.style.display = "none";
    }
    else{
    script.style.display = "flex";
    }
});