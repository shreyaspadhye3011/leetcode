// https://tinyurl.com/ybekq76c
const heador = xs => default_value => is_null(xs) ? default_value : head(xs); 
heador([2, [3, [4, [4, null]]]])(-1);
heador(null)(-1);