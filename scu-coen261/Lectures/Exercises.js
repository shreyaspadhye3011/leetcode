// Sol: Exercise 1.3 SICP JS

const square = a => a*a;

const sum_of_squares = a => b => square(a) + square(b); 

sum_of_squares(2)(3);

// const sum_larger_sqaures = a => b => c 
// => (a > b && b > c) ? sum_of_squares(a)(b);
// sum_larger_sqaures(2);

////// ********************** //////