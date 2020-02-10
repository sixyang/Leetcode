/* class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(n, ret):
            if n == 0:return 1                  #递归终止条件一定要写在最前面
            half = recursion(n//2, ret)         #先一步到胃，这一步是核心，也是男点 ( •̀ ω •́ )y

            #如果为偶数，就直接乘以一半的值，否则，结果为x**n-1，需要再乘以一个x
            if n % 2 == 0:return half * half
            else:return half * half * ret
        if n < 0:return 1/recursion(abs(n), x)
        else:return recursion(n, x)
        */

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    function recursion(n, x){
        if (n == 0) return 1;
        half = recursion(Math.floor(n/2), x);
        if (n%2 == 0) return half * half;
        else return half * half * x;
    };
    if (n<0) return 1/recursion(-n, x);
    else return recursion(n, x);
};
