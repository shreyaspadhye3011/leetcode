// sourceacademy: https://api2.sourceacademy.nus.edu.sg/sumofmultiples
// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// Sum of multiples - returns the sum of positive multples of 3 or 5 that are below a specified limit: 1000
const sum_of_multiples = limit => {
    const predicate = num => (num % 3 === 0 || num % 5 === 0);
    const add_multiples = num => sum => 
        num === limit ? sum : predicate(num)
        ? add_multiples(num+1)(sum + num)
        : add_multiples(num+1)(sum);
    return add_multiples(1)(0);
};

// tests
// sum_of_multiples(10);       // 23
sum_of_multiples(1000);     // 233168

// Answer: The sum of natural numbers divisible by 3 or 5 below 1000 is 233168