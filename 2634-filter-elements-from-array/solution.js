/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    emparr = []
    for(let i=0; i < arr.length; i++ ){
        if (fn(arr[i],i)){
            emparr.push(arr[i])
        }
    }
    return emparr
    
};