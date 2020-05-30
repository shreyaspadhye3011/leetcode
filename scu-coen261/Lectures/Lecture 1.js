// basic function
function square(x) {
    return x * x;
}

// normal inner function
function sum_of_squares(x, y) {
    function square(x) {
        return x * x;
    }
    return square(x) + square(y);
}

sum_of_squares(2, 3);

// currying -- function returning function
function a(x) {
    return function(y) {        // NOTE: Giving Error in Source. But it is fine
        return square(x) + square(y);
    };
}

// Currying - Source compatible
function a(x) {
    return (y) => {
        return square(x) + square(y);
    };
}
  
a(2)(3);

/// -------- Now all with proper ES6 ----------- ///
// basic function
const square = (x) => x * x;        // NOTICE that you don't need "return" keyword for single line statement

// normal inner function
const sum_of_squares = (x, y) => {
  const square = (x) => x * x;
  return square(x) + square(y);
};
display(sum_of_squares(2, 3));

// currying -- function returning function
// multi line
const a = (x) => {
  return (y) => square(x) + square(y);
};

// single line
const a = (x) => (y) => square(x) + square(y);

a(3)(3);



  
  
  