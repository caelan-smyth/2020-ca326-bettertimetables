function validateForm() {
    var x = document.forms["courseform"]["coursetitle"].value;
    if(x == "") {
        alert("Please input course name");
        return false;
    }
}