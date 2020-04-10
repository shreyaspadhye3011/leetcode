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