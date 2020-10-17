/*AI ChatBot by Anuj Upadhyay

Here is a real AI chatbot where you can train the bot yourself! Talk to it and decide wether or not its response is good!

I have already given it some training data to start with.

I hope you like it!

*/
alert("AI Chat Bot By Aritro Chakraborty");
alert("click yes or No if you are satisfied with your answer");
alert("Train Your AI");
window.addEventListener('load', function(){

var chat = document.getElementById("chatButton");
var no = document.getElementById("noButton");
var yes = document.getElementById("yesButton");
var txt = document.getElementById("textBox");
var confirm = document.getElementById("confirmation");
var help = document.getElementById("helpBox");
var helpBtn = document.getElementById("helpButton");
var trainingArea = document.getElementById("trainArea");
var botTalk = ["Hello! I hope you have a good day!","I am fine, thanks!","I have no name, but my creators name is Aritro Chakraborty!","42","I was created in October, 2020.","I am not human, I am a robot."];
var divArr=[];
var delayVar=0;

function newDiv(COLOR, TEXT){
var newdiv = document.createElement("div");

newdiv.style.width = "90%";
newdiv.style.height = "10%";
newdiv.style.background = COLOR;
if(COLOR=="green"){
	newdiv.style.left="53%";
}
else{
	newdiv.style.left="47%";
}
newdiv.style.bottom="15%";
newdiv.style.position="fixed";
newdiv.style.borderRadius="10px";
newdiv.style.transform="translate(-50%,0)";
newdiv.style.paddingLeft ="10px";
newdiv.style.paddingTop ="5px";
newdiv.style.fontFamily="	Verdana, Times, serif";
newdiv.innerHTML = TEXT;
newdiv.style.border = "1px solid black";
newdiv.style.color="white";
document.body.appendChild(newdiv);

divArr.push(newdiv);

for (y=0;y<divArr.length-1;y++){
	if (divArr[y].style.bottom=="15%"){
	divArr[y].style.bottom="28%";
}
else if (divArr[y].style.bottom=="28%"){
	divArr[y].style.bottom="41%";
}
else if (divArr[y].style.bottom=="41%"){
	divArr[y].style.bottom="54%";
}
else if (divArr[y].style.bottom=="54%"){
	divArr[y].style.bottom="67%";
}
else if (divArr[y].style.bottom=="67%"){
	divArr[y].style.bottom="80%";
}
else if (divArr[y].style.bottom=="80%"){
	divArr[y].style.bottom="93%";
}
else if (divArr[y].style.bottom=="93%"){
	divArr[y].style.bottom="106%";
}
else if(divArr[y].style.bottom=="106%"){
	divArr[y].style.display="none";
}
}


}
/*
newDiv("green","Who are you?");
newDiv("orange","I am a bot.");
*/
//***********Machine learning**************
var net = new brain.NeuralNetwork();
var trainData = [];
var maxLength = 0;
var remainingLength = 0;
var newInput;
var commands = 7;

//Greeting
trainData.push({ input: [1,0,0,0,1,1,1,1,0,0,1,0,0,0], output: {[1]: 1} }); //HI
trainData.push({ input: [1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0], output: {[1]: 1} }); //HEY
trainData.push({ input: [1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0], output: {[1]: 1} }); //HELLO
trainData.push({ input: [1,0,1,1,0,0,0,1,0,0,1,1,1,0], output: {[1]: 1} }); //Yo 
																													 
//How are you?
trainData.push({ input: [1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1], output: {[2]: 1} }); //How are you?

trainData.push({ input: [1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,1], output: {[2]: 1} }); //Are you ok?

//What is your name?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[3]: 1} }); //What is your name?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[3]: 1} }); //Whats your name?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[3]: 1} }); //Whats ur name?
trainData.push({ input: [1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[3]: 1} }); //Your name?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1], output: {[3]: 1} }); //Who are you?
trainData.push({ input: [1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[3]: 1} }); //Name?
																																																								   
//Meaning of life?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[4]: 1} }); //What is the meaning of life?
trainData.push({ input: [1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[4]: 1} }); //Meaning of life?

//How old are you?
trainData.push({ input: [1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1], output: {[5]: 1} }); //How old are you?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[5]: 1} }); //What is your age?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[5]: 1} }); //Whats your age?
trainData.push({ input: [1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1], output: {[5]: 1} }); //Whats ur age?
																																																									 
//Are you human?
trainData.push({ input: [1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1], output: {[6]: 1} }); //Are you human?
trainData.push({ input: [1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1], output: {[6]: 1} }); //human?

//Commands to fill up the arrays with zeros. All arrays must be of same length
for (j=0;j<trainData.length;j++){
	if (trainData[j].input.length > maxLength){
		maxLength = trainData[j].input.length;
	}
}
for (q=0;q<trainData.length;q++){
	if (trainData[q].input.length < maxLength){
		remainingLength = maxLength - trainData[q].input.length;
		zeroArray = Array(remainingLength).fill(0);
		trainData[q].input = trainData[q].input.concat(zeroArray);
	}
}

//Training
net.train(trainData, {
	log: false,
	logPeriod: 10,
	errorThresh: 0.0005,
}); //Using all the training data to train the AI


//Chat button
chat.addEventListener("click",function(){

if (txt.value != ""){

newDiv("green",txt.value);

var data = textToBinary(txt.value);

	var result = brain.likely(data, net);

	for (k=1;k<=botTalk.length;k++){

	if (result == k){
		delayVar=k;
		setTimeout(function(){
newDiv("orange",botTalk[delayVar-1]);

trainingArea.style.display="inline";
	
},800);
	}

	}

   help.style.display = "none";
	helpBtn.style.display = "none";
}
});

yes.addEventListener("click", function(){
	alert("Sweet!");
   	txt.value="";
   help.style.display = "none";
	helpBtn.style.display = "none";
	trainingArea.style.display="none";
})

no.addEventListener("click", function(){
	alert("Oh, I am sorry! What would be a good response to your input?");
divArr[divArr.length-1].style.backgroundColor="#ff6666"
help.style.display = "inline";
helpBtn.style.display = "inline";
})

helpBtn.addEventListener("click", function(){
trainingArea.style.display="none";
	botTalk.push(help.value);

	newInput = textToBinary(txt.value);

trainData.push({ input: newInput, output: {[commands]: 1} }); //user training data

commands = commands+1;

net = new brain.NeuralNetwork();

//Training the AI
net.train(trainData, {
	log: false,
	logPeriod: 10,
	errorThresh: 0.0005,
});

alert("Alright! Thanks for making me smarter!");

	txt.value="";
	help.value="";
   help.style.display = "none";
	helpBtn.style.display = "none";
})

function textToBinary(text){
	//Storing all letters as binary numbers for AI
text = text.toUpperCase();
	var data = [];
	
	for (i=0;i<text.length;i++){
		
		if ( text[i]=="A"){
			data = data.concat([1,0,0,0,0,0,0]);
		}
		else if (text[i]=="B"){
			data = data.concat([1,0,0,0,0,0,1]);
		}
		else if (text[i]=="C"){
			data = data.concat([1,0,0,0,0,1,0]);
		}
		else if (text[i]=="D"){
			data = data.concat([1,0,0,0,0,1,1]);
		}
		else if (text[i]=="E"){
			data = data.concat([1,0,0,0,1,0,0]);
		}
		else if (text[i]=="F"){
			data = data.concat([1,0,0,0,1,0,1]);
		}
		else if (text[i]=="G"){
			data = data.concat([1,0,0,0,1,1,0]);
		}
		else if (text[i]=="H"){
			data = data.concat([1,0,0,0,1,1,1]);
		}
		else if (text[i]=="I"){
			data = data.concat([1,0,0,1,0,0,0]);
		}
		else if (text[i]=="J"){
			data = data.concat([1,0,0,1,0,0,1]);
		}
		else if (text[i]=="K"){
			data = data.concat([1,0,0,1,0,1,0]);
		}
		else if (text[i]=="L"){
			data = data.concat([1,0,0,1,0,1,1]);
		}
		else if (text[i]=="M"){
			data = data.concat([1,0,0,1,1,0,0]);
		}
		else if (text[i]=="N"){
			data = data.concat([1,0,0,1,1,0,1]);
		}
		else if (text[i]=="O"){
			data = data.concat([1,0,0,1,1,1,0]);
		}
		else if (text[i]=="P"){
			data = data.concat([1,0,0,1,1,1,1]);
		}
		else if (text[i]=="Q"){
			data = data.concat([1,0,1,0,0,0,0]);
		}
		else if (text[i]=="R"){
			data = data.concat([1,0,1,0,0,0,1]);
		}
		else if (text[i]=="S"){
			data = data.concat([1,0,1,0,0,1,0]);
		}
		else if (text[i]=="T"){
			data = data.concat([1,0,1,0,0,1,1]);
		}
		else if (text[i]=="U"){
			data = data.concat([1,0,1,0,1,0,0]);
		}
		else if (text[i]=="V"){
			data = data.concat([1,0,1,0,1,0,1]);
		}
		else if (text[i]=="W"){
			data = data.concat([1,0,1,0,1,1,0]);
		}
		else if (text[i]=="X"){
			data = data.concat([1,0,1,0,1,1,1]);
		}
		else if (text[i]=="Y"){
			data = data.concat([1,0,1,1,0,0,0]);
		}
		else if (text[i]=="Z"){
			data = data.concat([1,0,1,1,0,0,1]);
		}
		else if (text[i]=="?"){
			data = data.concat([1,1,1,1,1,1,1]);
		}
	}
	//Used the code below to be able to read long arrays
	//console.log(data.toString());

	//Fill user input array with zeros to get correct length
	if (data.length < maxLength){
		remainingLength = maxLength - data.length;
		zeroArray = Array(remainingLength).fill(0);
		data = data.concat(zeroArray);
	}
	return data;
}
});