// Reference: https://www.guru99.com/javascript-interview-questions-answers.html

// Timeout: call a function after a delay
setTimeout(function(){
  // code to exdcute after delay
}, 3000); 

// Interval: call a function repeatedly after a set interval
let count = 0;
let cutOffCount = 50;   // cut off interval after 50 calls
let intervalFn = setInterval(function() {
  if (true /*some condition that you meet*/) {
    clearInterval(intervalFn);
  } else {
    if (count === cutOffCount) {
      clearInterval(intervalFn);
    }
    count++;
  }
}, 500);

// Asynchronous nature and callbacks
const fs = require('fs');
fs.readFile('./script.js', function(error, data) {
  // error is null if no error occurred, but an Error object if it did
  if (error) {
   throw error;
  }
  // the file data will be passed into the callback if no error was thrown
  console.log(data);
});

// Datatypes: 
Number
String
Boolean
Object
Undefined

// convert different base number to integer `parseInt ("<number>", <original base>);`
parseInt ("4F", 16);

// detect machine / user agent details
navigator.userAgent   // Full user agent
navigator.platform    // OS
navigator.appName     // browser application

// declaring global var in JS
globalVariable = "Test";

// Styling
document.getElementById("myText").style.fontSize = "20";
document.getElementById("myText").style.display = "none";
document.getElementById("myText").className = "anyclass";
document.getElementById("myText").classList.add("anyclass");
document.getElementById("myText").classList.remove("anyclass");

var newP = document.createElement("p"); 
var textNode = document.createTextNode(" This is a new text node"); 
newP.appendChild(textNode); 
document.getElementById("firstP").appendChild(newP);
//.replaceChild(existing.parentNode.firstChild, newP)

// delete key with its value
var student= {age:20, batch:"ABC"};
delete student.age;

// storing items
localStorage.setItem("key", "value");
localStorage.getItem("key");
sessionStorage.setItem("key", "value");   // cleared when user quits the 
sessionStorage.getItem("key");

// Void(0) is used to call another method without refreshing the page.

// 34. What is the data type of variables of in JavaScript?
// A: All variables in the JavaScript are object data types.