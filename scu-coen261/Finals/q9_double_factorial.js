const double_factorial = n => {
    const double_fact_iter = (num, product) => {
        return num === 0 || num === -1 ? product : double_fact_iter(num-2, num*product);
    };
    return double_fact_iter(n, 1);
};