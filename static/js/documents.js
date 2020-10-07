function check_ex() {
    var list = ['pdf', 'docx', 'doc', 'xml', 'xlsx']
    var fullPath = document.getElementById("id_document").value;
    if (fullPath) {
        var startIndex =
            fullPath.indexOf("\\") >= 0
                ? fullPath.lastIndexOf("\\")
                : fullPath.lastIndexOf("/");
        var filename = fullPath.substring(startIndex);
        if (filename.indexOf("\\") === 0 || filename.indexOf("/") === 0) {
            filename = filename.substring(1);
        }
        var x = filename.split('.').pop();
        if (list.includes(x) == false) {
            alert(x + ' format is not allowed, use only files with (word,exel,pdf) extensions');
            location.reload()
        };

    }
}

