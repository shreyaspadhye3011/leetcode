// Reference: https://www.guru99.com/javascript-interview-questions-answers.html

// Arrays
let arr = [1, 2];
arr.push(3);    // arr is [1, 2, 3]
// .pop()       // removes and returns from end of array eg 3, here
arr.unshift(0); // arr is [0, 1, 2, 3] // append at beginning
var ar = ['zero', 'one', 'two', 'three']; ar.shift(); // returns "zero" (removes from beginning)

console.log(apps);

// Filter JS array
myarr = [32, 33, 16, 40]
console.log('myarr', myarr.filter(val => val > 18));   // myarr [ 32, 33, 40 ]

// Filter JS objects
const data = [
  {
    name: 'Bob',
    gender: 'male',
    age: 34,
  },
  {
    name: 'Carol',
    gender: 'female',
    age: 36,
  },
  {
    name: 'Ted',
    gender: 'male',
    age: 38,
  },
  {
    name: 'Alice',
    gender: 'female',
    age: 40,
  },
];
const arr1 = data.filter(d => d.age > 37);
console.log('arr1', arr1); 
// arr1 [
//   { name: 'Ted', gender: 'male', age: 38 },
//   { name: 'Alice', gender: 'female', age: 40 }
// ]
const arr2 = data.filter(d => d.gender === 'female');
console.log('arr2', arr2);
// arr2 [
//   { name: 'Carol', gender: 'female', age: 36 },
//   { name: 'Alice', gender: 'female', age: 40 }
// ]
const ageAndGender = d => d.age > 37 && d.gender === 'female';
const arr3 = data.filter(ageAndGender);
console.log('arr3', arr3);
// arr3 [ { name: 'Alice', gender: 'female', age: 40 } ]

// Array map
const array1 = [1, 4, 9, 16];
// pass a function to map
const map1 = array1.map(x => x * 2);
console.log(map1);
// expected output: Array [2, 8, 18, 32]

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

// Closures
// Function for getting the id of a dom element,
// giving it a new, unique id if it doesn't have an id yet
const getUniqueId = (() => {
  let nextGeneratedId = 0;
  return element => {
    if (!element.id) {
      element.id = `generated-uid-${nextGeneratedId}`;
      nextGeneratedId++;
    }
    return element.id;
  };
})();

// Lambda / ES6 function style
var msg = (x,y) => { 
  console.log(x, y);
} 
msg(10, 20)
// Notice that paranthesis are optional for single argument
var msg1 = x => { 
  console.log(x);
} 
msg1(10)
// Notice that braces are optional for single statement
var disp = () => console.log("Hello World");



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
// cookies
document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";   // save cookie
// retrieve cookie
document.cookie

// Void(0) is used to call another method without refreshing the page.

// 34. What is the data type of variables of in JavaScript?
// A: All variables in the JavaScript are object data types.