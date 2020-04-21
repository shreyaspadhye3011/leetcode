// https://codology.net/post/sicp-solution-exercise-1-11/

function f (n) {
  if (n < 3) {
    return n;
  } else {
      return (f (n - 1)) + (2 * (f (n - 2))) + (3 * (f (n - 3)));
  }
}

f(4);  

// define f(n) {
//     if (n < 3) {
//       n
//   } else {
//       (f (n - 1)) + (2 * (f (n - 2))) + (3 * (f (n - 3)))
//   }
// }

// SCM: 1.11.b 
(define (f2 n)
  (define (f-iter a b c n)
    (if (= n 0)
        a
        (f-iter b c (+ c (* 2 b) (* 3 a)) (- n 1))))
  (f-iter 0 1 2 n))


// JS: 1.11.b
function sub() {
    const args = [].slice.call(arguments);
    return args.slice(1).reduce((a, b) => a - b, args[0]);
};
function mult() {
    return [].slice.call(arguments).reduce((a, b) => a * b, 1);
};
function plus() {
    return [].slice.call(arguments).reduce((a, b) => a + b, 0);
};
function eq(a, b) {
    return a === b;
};
function f2(n){
    function f_iter(a,b,c,n) {
        return (eq(n,0)) ? (a) : (f_iter(b,c,plus(c,mult(2,b),mult(3,a)),sub(n,1)));
    }
    return f_iter(0,1,2,n);
}