function euclidean_distance(f, g, precision) { 
    function iter(sum, x) {
        return x == precision ? sum
            : iter(sum + (Math.abs(f(x) - g(x))**2), x+1);
    }
    return iter(0, 0) ** (1/2);
}

console.log(euclidean_distance(Math.sin, Math.cos, 100));
  


// function eucDistance(a, b) {
//     return a
//         .map((x, i) => Math.abs( x - b[i] ) ** 2) 
//         .reduce((sum, now) => sum + now) 
//         ** (1/2)
// }

// let euc = eucDistance([1,2,5,6,4.6], [4,6,33,45,2.5]);
// console.log(euc);