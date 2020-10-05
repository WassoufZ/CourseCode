
var count = 0;


document.getElementById("add_image").onclick = function (ev) {
    var image = document.getElementById("images");
    var preview = document.getElementById('show');
    var newInput = document.createElement("input");
    var button = document.createElement("button");
    var div = document.createElement("div");

    count++;

    if (count > 3) {
        document.getElementById("add_image").classList.add('disabled')
        document.getElementById("add_image").disabled = true;
    };

    div.className = 'oneline'
    div.id = "file" + count

    newInput.type = "file";
    newInput.name = "file[]";
    newInput.id = "file" + count;
    newInput.style.display = 'inline-block';

    button.type = "button";
    button.id = "file" + count;
    button.innerHTML = "<i class='icon-trash position-center'></i>";
    button.style.display = 'inline-block';
    button.addEventListener('click', MyFunc);


    newInput.onchange = function (ev1) {
        if (this.files && this.files[0]) {
            var fileReader = new FileReader();

            fileReader.onload = function (ev2) {
                preview.src = ev2.target.result;
                if (count < 4) {
                    jQuery(function () {
                        jQuery('#add_image').click();
                    });
                };

            };
            fileReader.readAsDataURL(this.files[0])
        }
    };

    div.appendChild(newInput);
    div.appendChild(button);
    image.appendChild(div);

};

document.getElementById("remove_image").onclick = function () {
    var all = document.getElementById('images');
    while (all.firstChild) {
        all.removeChild(all.lastChild);
    };
    count = 0;
    document.getElementById("add_image").classList.remove('disabled');
    document.getElementById("add_image").disabled = false;

};


jQuery(function () {
    jQuery('#add_image').click();
});

function MyFunc() {
    document.getElementById(this.id).remove();
    document.getElementById("add_image").classList.remove('disabled');
    document.getElementById("add_image").disabled = false;
    count--;
};
