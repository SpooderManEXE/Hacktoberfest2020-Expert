//find you're blink or not

var x = "Jisoo";
blackPink(x);

function blackPink(name){
    var listName =['Jisoo','Jennie','Lisa','Rose','jisoo','jennie','lisa','rose','ROSÉ'];
    var blink = listName.indexOf(name);
    if(blink === -1){
      return console.log("You not BLINK");
    } else {
      return console.log("You are BLINK!!");
    }
}