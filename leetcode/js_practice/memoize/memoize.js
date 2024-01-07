function memoize(fn) {
    let cache = {};

    return function(...args) {
        if (args in cache) {
            return cache[args];
        }

        else {
            cache[args] = fn(...args);
            
            return cache[args];
        }
    }
}
