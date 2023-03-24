function expandNavbar() {
    var x = document.getElementById("myTopnav");
    if (x.className === "col-12 topnav") {
        x.className += " responsive";
    } else {
        x.className = "col-12 topnav";
    }
}
