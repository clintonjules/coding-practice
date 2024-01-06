var compose = function(functions) {
    
    return function(x) {
        if (functions.length == 0) return x;

        let fx = x;

        for (let i=functions.length-1;i>=0;i--) {
            fx = functions[i](fx);
        }

        return fx;
    }
};
