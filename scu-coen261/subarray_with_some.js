// returns the sub-array which adds up to the target sum, otherwise returns blank array [] 
function find_subarray_with_sum(array, start, end, sum, target) {
    console.log(start, end, sum)
    if (sum < target) {
        if (end === array.length) return false;
        end += 1;
        sum += array[end];
    } else if (sum > target) {
        if (start === end) return false;
        start += 1;
        sum -= array[start];
    }
    if (sum === target) return true;
    find_subarray_with_sum(array, start, end, sum, target)
}

console.log(find_subarray_with_sum([1, 4, 20, 3, 10, 5], 0, 0, 0, 33));

// function find_subarray_with_sum(array, start=0, end=0, sum=0, target) {
//     return sum === target ? array.slice(0, end+1) 
//     : sum < target ?
// }