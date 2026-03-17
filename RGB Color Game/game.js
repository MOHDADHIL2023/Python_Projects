var NumOfSquares = 6
var color = generateRandomColors(NumOfSquares);
var squares = document.querySelectorAll(".SQUARE");
var pickedcolor = pickColor();
var displaycolor = document.querySelector("#color-display");
var messagedisplay = document.querySelector("#MESSAGE");
var h1 = document.querySelector("#h1");
var reset = document.querySelector("#reset");
var easybutton = document.querySelector("#easy");
var hardbutton = document.querySelector("#hard");

easybutton.addEventListener("click", function(){
    easybutton.classList.add("selected");
    hardbutton.classList.remove("selected");
    NumOfSquares = 3;
    color = generateRandomColors(NumOfSquares);
    pickedcolor = pickColor();
    displaycolor.textContent = pickedcolor;
    for(var i=0; i < squares.length; i++){
        if(color[i]){
            squares[i].style.backgroundColor = color[i];
        }
        else{
            squares[1].style.display = "none";
        }
    }
})

hardbutton.addEventListener("click", function(){
    easybutton.classList.remove("selected");
    hardbutton.classList.add("selected");
    NumOfSquares = 6;
    color = generateRandomColors(NumOfSquares);
    pickedcolor = pickColor();
    displaycolor.textContent = pickedcolor;
    for(var i=0; i<squares.length; i++){
        squares[i].style.backgroundColor = color[i];
        squares[i].style.display = "block";
    }
})

reset.addEventListener("click", function(){
    console.log("clicked")
    color = generateRandomColors(NumOfSquares);
    pickedcolor = pickColor();
    displaycolor.textContent = pickedcolor;
    reset.textContent = "New Colors"

    messagedisplay.textContent = "";
    for(var i=0; i<squares.length; i++){
        squares[i].style.backgroundColor = color[i];
    }
    h1.style.backgroundColor = "steelblue";
})

displaycolor.textContent = pickedcolor;
for (var i=0; i<squares.length; i++){
    squares[i].style.backgroundColor = color[i];
    squares[i].addEventListener("click", function(){
        var clickedcolor = this.style.backgroundColor;
        console.log(pickedcolor,clickedcolor)
        if(clickedcolor === pickedcolor){
            messagedisplay.textContent = "Correct";
            changecolors(clickedcolor);
            h1.style.backgroundColor = clickedcolor;
            reset.textContent = "Play Again?";
        }
        else{
            this.style.backgroundColor = "grey"
            messagedisplay.textContent = "Try Again"
        }
    })
}

function changecolors(colors){
    for(var i=0; i < squares.length; i++){
        squares[i].style.backgroundColor = colors
    }
}

function pickColor(){
    var random = Math.floor(Math.random() * color.length);
    return color[random];
}

function generateRandomColors(num){
    var arr = [];
    for(var i=0; i<num; i++){
        arr.push(THREERANDOMVALUES());
    }
    return arr;
}

function THREERANDOMVALUES(){
    var r= Math.floor(Math.random() * 256);
    var g= Math.floor(Math.random() * 256);
    var b= Math.floor(Math.random() * 256);

    return "rgb("+r+","+g+","+b+")";
}