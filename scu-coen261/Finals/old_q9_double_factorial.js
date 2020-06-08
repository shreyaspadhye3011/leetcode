// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// sourceacademy: https://api2.sourceacademy.nus.edu.sg/doublefacto

// Accepts a number and returns double factorial as described here: https://mathworld.wolfram.com/DoubleFactorial.html
const double_factorial = n => {
    const double_fact_iter = (num, product) => {
        return num < -1 ? "not defined" : (num === 0 || num === -1) ? product : double_fact_iter(num-2, num*product);
    };
    return double_fact_iter(n, 1);
};

// tests
display(double_factorial(-1));      // 1
display(double_factorial(4));       // 8
display(double_factorial(5));       // 15
display(double_factorial(6));       // 48
display(double_factorial(7));       // 105
double_factorial(-7);               // not defined

