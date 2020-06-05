// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// sourceacademy: https://api2.sourceacademy.nus.edu.sg/diffsquares

// get sum of first n natural numbers
const sum_of_n = n => n * (n+1) / 2;
const square_of_sum = n => sum_of_n(n) * sum_of_n(n);
// get sum of square of n natural numbers
const sum_of_squares = n => ((2*n+1) * n * (n+1)) / 6;
const difference_in_squares = n => square_of_sum(n) - sum_of_squares(n);

// tests
// difference_in_squares(10);    // 2640
difference_in_squares(100);     // 25164150