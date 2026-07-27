/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    value = init
    return{
    increment: function (){
        return value+=1
    },
    decrement: function (){
        return value -=1
    },
    reset: function (){
        value = init
        return init
    }}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */