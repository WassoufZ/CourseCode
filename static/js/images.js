
var count = 0;

document.getElementById("add_image").onclick = function (ev) {
    var image = document.getElementById("images");
    var preview = document.getElementById('show');
    var newInput = document.createElement("input");
    count++;
    if(count > 3){
        document.getElementById("add_image").classList.add('disabled')
        document.getElementById("add_image").id = 'none'
    };

    newInput.type = "file";
    newInput.name = "file[]";
    newInput.id = "file";
    newInput.className = 'btn btn-default btn-rounded btn-xs legitRipple';
    


    

    var br = document.createElement('br')
    newInput.onchange = function (ev1) {
        if (this.files && this.files[0]) {
            var fileReader = new FileReader();

            fileReader.onload = function (ev2) {
                preview.src = ev2.target.result;

            };
            fileReader.readAsDataURL(this.files[0])
        }
    };
    image.appendChild(newInput);
    image.appendChild(br);

}


