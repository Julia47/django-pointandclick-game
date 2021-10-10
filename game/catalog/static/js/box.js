function setStyleBox(checkbox, id){
    var top = 14 + (id * 6.4) - id;
    var top2 = top + 2.5;
    if (checkbox.checked == true){
        var element = document.getElementById("box-" + (id + 1).toString());
        element.style.width = "4.3%";
        element.style.cursor = "pointer";
        element.style.position = "absolute";
        element.style.background = "none";
        element.style.marginTop = top.toString() + '%';
        element.style.marginLeft = "23%";
        element.style.zIndex = "3";
    } else {
        var element = document.getElementById("box-" + (id + 1).toString());
        element.style.width = "4.4%";
        element.style.cursor = "pointer";
        element.style.position = "absolute";
        element.style.background = "none";
        element.style.marginTop = top2.toString() + '%';
        element.style.marginLeft = "27%";
        element.style.zIndex = "3";
    }
}


var test_b = [false, true, true, true, false, true];

function checkboxes(inputs){
    if(inputs.length!=test_b.length){
        return false;
    }else{
    for(var i=0;i<inputs.length;i++)
        if(test_b[i]!=inputs[i].checked){
            return false;
        }
        return true;
    }
}



function checkAll() {
    var inputs = document.querySelectorAll('.box');
    for (var i = 0; i < inputs.length; i++) {
        setStyleBox(inputs[i], i)
    }
    if (checkboxes(inputs)){
        location.href="/catalog/box_right";
    }
}

window.addEventListener("click", function(){
    checkAll();
});

checkAll();


