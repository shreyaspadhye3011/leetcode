const fib = n => {
  const fib_iter = n => a => b => count => {
      return count === n ? b : fib_iter(n)(b)(a+b)(count+1);
  };
  return n === 1 ? 0 : fib_iter(n)(0)(1)(2);  
};

fib(4);