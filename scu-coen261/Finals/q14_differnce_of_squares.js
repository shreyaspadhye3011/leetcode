// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// get sum of first n natural numbers
const sum_of_n = n => n * (n+1) / 2;
const square_of_sum = n => sum_of_n(n) * sum_of_n(n);
// get sum of square of n natural numbers
const sum_of_squares = n => ((2*n+1) * n * (n+1)) / 6;
const difference_in_squares = n => square_of_sum(n) - sum_of_squares(n);

difference_in_squares(10);      // 2640
display(sum_of_n(100));         // 5050
display(square_of_sum(100));    // 25502500
display(sum_of_squares(100));   // 338350
difference_in_squares(100);     // 25164150

25502500 - 338350;              // 25164150