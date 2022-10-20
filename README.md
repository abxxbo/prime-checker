# prime-checker
A python script that checks if `n` is prime. It does not use the `math` library.
The only library that this app uses is `sys` (for `sys.argv`)


# Details

## How does it check primes?
Using C. P. Willans's 1964 algorithm, we can do something like this:
$$f(x)=\left\lfloor\left(\cos\left(\frac{(x-1)!+1}{x}\right)\pi\right)^2\right\rfloor$$

This will return a $0$ or a $1$. It will return $1$ if $n$ is prime or $n=1$. If it returns $0$, it's composite (not prime!).

## How do you use $\cos$ without using `math.cos()`?
Using a Taylor series:
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - ...$$
