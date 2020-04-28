const Y = g => (x => g(x(x)))(x => g(x(x)));

// Y(f) = f(Y(f))
function Y(f) {
    function innerfunction(x) {
        const res = v => {
           return x(x)(v);
        };
        return f(res);
    }
    return innerfunction(innerfunction);
}