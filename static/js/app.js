var myHeader = document.querySelector('h1');
myHeader.style.color = 'white';
function createColorHeader(){
    var letters='0123456789ABCDEF';
    var color='#';
    for (i=0;i<6;i++){
        color+= letters[Math.floor(Math.random()*16)]
    }
    return color;
}
function changeColorHeader(){
    inputColor=createColorHeader();
    myHeader.style.color=inputColor;
}
setInterval("changeColorHeader()",500);