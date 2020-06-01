// https://tinyurl.com/coen261-3

// -- Newton's method of square-root
// My:
const abs = x => x >= 0 ? x : -x;
const is_good_enough = guess => x => abs((guess * guess) - x) < 0.00001;
const sqrt_helper = x => guess => is_good_enough(guess)(x) ? guess : sqrt_helper(x)((guess + x/guess)/2);
const sqrt = x => sqrt_helper(x)(x/2);
sqrt(3);     // 1.7320508100147274

// Prof Vlad:
function abs(x) { return x >= 0 ? x : -x; }
function square(x) { return x * x; }
function good_enough(guess, x) {
  return abs(square(guess) - x) < 0.00001;
}
function average(x,y) { return (x + y) / 2; }
function improve(guess, x) { return average(guess, x / guess); }
function sqrt_iter(guess, x) {
  return good_enough(guess, x)
         ? guess
         : sqrt_iter(improve(guess, x), x);
}
function sqrt(x) { return sqrt_iter(x/2, x); }
sqrt(sqrt(100) + sqrt(36));
// IMP: Abstraction (Hide details!)
// Note: How beautifully the code is strucured and how readable it is
// It is not just about writing less code but it is about writing beautiful / readable code

// ------------------------------------------------ //
// Factorial - Recursive
const factorial = n => n === 0 ? 1 : n * factorial(n-1);
factorial(5);   // 120

// ------------------------------------------------ //
// Factorial - Tail recursion optimization / Iteration
const factorial = n => {
    const fact_iter = (num, product) => {
        return num === 0 ? product : fact_iter(num-1, num*product);
    };
    return fact_iter(n, 1);
};

factorial(6);


