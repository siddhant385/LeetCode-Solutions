/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let transformed = []
    for(let i=0; i < arr.length; i++){
        transformed.push(fn(arr[i],i))
    }
    return transformed
};