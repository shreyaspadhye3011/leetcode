
const fib = n => {
  const fib_iter = n => a => b => count => {
      return count === n ? b : fib_iter(n)(b)(a+b)(count+1);
  };
  return n < 1 ? "Not defined." : n === 1 ? 1 : fib_iter(n)(1)(2)(2);  
};

fib(0);