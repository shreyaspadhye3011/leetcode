// Sol: Exercise 1.3 SICP JS

const square = a => a*a;
const sum_of_squares = a => b => square(a) + square(b); 
sum_of_squares(2)(3);

// return sum of squares for two larger numbers
const sum_larger_sqaures = a => b => c => 
(a >= b && b >= c) 
? sum_of_squares(a)(b)
: (b >= c && c >= a) 
? sum_of_squares(b)(c)
: sum_of_squares(a)(c);

sum_larger_sqaures(3)(3)(2);

////// ********************** //////

// Exercise 1.5 SICP JS
function p() {
    return p();
}

function test(x, y) {
    return x === 0 ? 0 : y;
}

test(0, p());   // Source / JS is applicative order as it results in infinte loop. Normal order wouldn't even need to evaluate p() as ternary will result in 0. -- Check solution in book if confused

// Normal order: Returns 0
// Applicative order: infinte loop