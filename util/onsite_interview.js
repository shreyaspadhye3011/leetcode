someAsyncFunction
.then({
    // do somethiong when it succeeds
})
.catch({

})
.finally({

})

// const someAsyncFunction = new Promise(resolve, reject) {
//     // API call
//     if(api_call_succeeded) {
//         resolve()
//     }
// } 

var myPromise = function () {
    const promise = new Promise((resolve, reject) => {
        const randomNumber = Math.random();
        setTimeout(() => {
        if(randomNumber < .6) {
            resolve('All things went well!');
            console.log('OK');
        } else {
            reject(new Error('Something went wrong'));
        }
      }, 1000);
    });
}

// sentence has spaces. write an algorithm to check if sentence is palindrome
// sentence.split("")
// Input: "words sdrow"
// Output: true

// Input: "%w ords sdrow"
// Output: true

// Input: "A word"
// Output: false


function is_Palindrome(sentence) {
    let lo = 0;
    let hi = sentence.length - 1;
    sentence.replace("%","");
    // check palindrome
    while(lo < hi) {
        if (sentence[lo] !== sentence[hi]) {
            return false;
        } 
        lo += 1;
        hi -= 1;
    }
    return true;
}
// O(n)

// _____


var words1 = ["hello","later"], 
order1 = "hlabcdefgijkmnopqrstuvwxyz";

// Input: hello, hellp
// true

// loop over each index associted (words1[0][0] < words1[1][0]) ? false : continue
// if the order is reversed at any point, return false

// lengths match
// 2 strings in the list
function isCustomSorted(list, order) {
    let word1 = list[0];
    let word2 = list[1];
    // iterate over the characters in the word
    for (let idx in word1) {
        // idxof("l") < indxof("h") -> return false;
        if (order.indexof(word2[idx]) < order.indexof(word1[idx])) {
            return false;
        }
    }
}


