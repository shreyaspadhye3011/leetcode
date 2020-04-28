function getSubset(array, sum) {
    let resultVar = false;
    function iter(temp, delta, index) {
        if (!delta) {
            resultVar = true;
            result.push(temp);
            // console.log("return True")
            return;
        }
        if (index >= array.length) {
            // resultVar = false;
            // console.log(">>> return Falsw")
            return;
        }
        iter(temp.concat(array[index]), delta - array[index], index + 1);
        if (!temp.length) iter(temp, delta, index + 1);
        // console.log("call-"+temp.length)
    }

    var result = [];
    iter([], sum, 0);
    console.log("Res: "+resultVar);
    console.log(result);
    // return result;
}

// function getSubset2(array, sum) {
//     function iter(temp, delta, index) {
//         if (!delta) result.push(temp);
//         if (index >= array.length) return;
//         iter(temp.concat(array[index]), delta - array[index], index + 1);
//         if (!temp.length) iter(temp, delta, index + 1);
//     }

//     var result = [];
//     iter([], sum, 0);
//     return result;
// }


console.log(getSubset([2, 4, 45, 6, 0, 19], 51));       // [2, 4, 45], [45, 6], [45, 6, 0]
console.log(getSubset([1, 11, 100, 1, 0, 200, 3, 2, 1, 280], 280)); // [280]
console.log(getSubset([1, 3, 6, 11, 1, 5, 4], 4));     // [ [ 1, 3 ], [ 4 ] ]
console.log(getSubset([1, 3, 6, 11, 1, 5, 4], 14));     // [ [ 1, 3 ], [ 4 ] ]