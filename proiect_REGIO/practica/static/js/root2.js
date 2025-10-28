document.addEventListener("DOMContentLoaded", () => {

    // Add event listeners to the buttons for redirection
    document.getElementById("formular-button").onclick = () => {
        window.location.href = "/formular_bypass/";
    };
    document.getElementById("profil-button").onclick = () => {
        window.location.href = "/users/profil/";
    };
    document.getElementById("logout-button").onclick = () => {
        window.location.href = "/logout/";
    };
});
