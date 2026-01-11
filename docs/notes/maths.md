# Mathematics Fundamentals for DSA

A compact reference for math topics frequently used in Data Structures & Algorithms and common LeetCode problems.

---

## 1. Divisors

**Definition:** A divisor of a number $n$ is any integer $d$ such that $n \bmod d = 0$.

**Examples:**
- Divisors of 6: 1, 2, 3, 6
- Divisors of 12: 1, 2, 3, 4, 6, 12

**Intuition:** Every number can be expressed via its divisors. To list divisors efficiently, iterate up to $\sqrt{n}$ and pair $d$ with $n/d$.

**Facts:**
- If $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, then the number of divisors is $(a_1+1)(a_2+1)\cdots(a_k+1)$.
- Sum of divisors $\sigma(n) = \prod_i \frac{p_i^{a_i+1}-1}{p_i-1}$.

**Code (list divisors):**
```python
import math

def divisors(n):
    ds = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)
```

**LeetCode practice:**
- The Kth Factor of n (1492): https://leetcode.com/problems/the-kth-factor-of-n/
- Self Dividing Numbers (728): https://leetcode.com/problems/self-dividing-numbers/

---

## 2. Prime Numbers

**Definition:** A prime is a natural number $>1$ with no positive divisors other than 1 and itself.

**Intuition:** Primes are the building blocks of integers (Fundamental Theorem of Arithmetic).

**Algorithms:**
- Trial division up to $\sqrt{n}$ for primality.
- Sieve of Eratosthenes to mark all primes $\le N$ in $O(N\log\log N)$.

**Code (primality test):**
```python
import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True
```

**LeetCode practice:**
- Count Primes (204): https://leetcode.com/problems/count-primes/
- Prime arrangements related: Power of Three (326): https://leetcode.com/problems/power-of-three/

---

## 3. Prime Factorization

**Definition:** Break $n$ into primes multiplying to $n$.

**Examples:**
- $12 = 2^2 \times 3^1$
- $60 = 2^2 \times 3^1 \times 5^1$

**Algorithm:** Trial division with division while divisible; if remainder $>1$, it’s prime.

**Code:**
```python
import math

def prime_factors(n):
    fs = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d)
            n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs
```

---

## 4. Greatest Common Divisor (GCD)

**Definition:** Largest integer dividing both $a$ and $b$.

**Algorithm:** Euclid’s algorithm: $\gcd(a,b)=\gcd(b, a\bmod b)$.

**Code:**
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

**LeetCode practice:**
- Greatest Common Divisor of Strings (1071): https://leetcode.com/problems/greatest-common-divisor-of-strings/

---

## 5. Least Common Multiple (LCM)

**Definition:** Smallest number divisible by both $a$ and $b$.

**Formula:** $\operatorname{lcm}(a,b)=\frac{a\cdot b}{\gcd(a,b)}$.

**Code:**
```python
def lcm(a, b):
    g = gcd(a, b)
    return a // g * b
```

---

## 6. Sum Formulas

- $1 + 2 + \cdots + n = \frac{n(n+1)}{2}$
- $1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$
- $1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2$

**LeetCode practice:**
- Sum of Square Numbers (633): https://leetcode.com/problems/sum-of-square-numbers/

---

## 7. Missing Numbers

**Problem:** Given numbers $1..n$ with some missing, find the missing values.

**Methods:**
- Sum formula: missing $= \frac{n(n+1)}{2} - \sum\text{(array)}$.
- XOR: XOR all $1..n$ and XOR with array; result is missing when exactly one missing.

**LeetCode practice:**
- Missing Number (268): https://leetcode.com/problems/missing-number/
- Find All Numbers Disappeared in an Array (448): https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
- Set Mismatch (645): https://leetcode.com/problems/set-mismatch/

---

## 8. Digit Extraction

**Techniques:**
- Last digit: `n % 10`
- Remove last: `n //= 10`

**Applications:** palindrome check, sum of digits, happy numbers.

---

## 9. Reverse a Number

**Algorithm:**
```python
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
```

**LeetCode practice:**
- Reverse Integer (7): https://leetcode.com/problems/reverse-integer/

---

## 10. Palindrome Numbers

**Definition:** Same forwards and backwards.

**Check:** Reverse and compare.

**LeetCode practice:**
- Palindrome Number (9): https://leetcode.com/problems/palindrome-number/

---

## 11. Armstrong Numbers

**Definition:** Sum of digits^$k$ equals the number; $k=$ number of digits.

**Example:** 153 $\to 1^3 + 5^3 + 3^3 = 153$.

**Code:**
```python
def is_armstrong(n):
    s = str(n)
    k = len(s)
    return sum(int(c) ** k for c in s) == n
```

---

## 12. Happy Numbers

**Definition:** Replace number by sum of squares of digits until it becomes 1 (happy) or loops (not happy).

**Tip:** Detect cycles using a set or Floyd’s cycle method.

**Code:**
```python
def is_happy(n):
    seen = set()
    def next_val(x):
        return sum((int(c) ** 2) for c in str(x))
    while n != 1 and n not in seen:
        seen.add(n)
        n = next_val(n)
    return n == 1
```

**LeetCode practice:**
- Happy Number (202): https://leetcode.com/problems/happy-number/

---

## 13. Combinatorics Basics

**Formulas:**
- Permutation: $P(n,r) = \frac{n!}{(n-r)!}$
- Combination: $C(n,r) = \frac{n!}{r!(n-r)!}$

**LeetCode practice:**
- Combinations (77): https://leetcode.com/problems/combinations/
- Permutations (46): https://leetcode.com/problems/permutations/
- Combination Sum (39): https://leetcode.com/problems/combination-sum/
- Pascal’s Triangle (118): https://leetcode.com/problems/pascals-triangle/
- Pascal’s Triangle II (119): https://leetcode.com/problems/pascals-triangle-ii/
- Unique Paths (62): https://leetcode.com/problems/unique-paths/

---

## 14. Sieve of Eratosthenes

**Idea:** Generate primes $\le N$ efficiently by marking multiples starting at $i^2$ for each prime $i$.

**Code:**
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
        p += 1
    return [i for i in range(2, n + 1) if is_prime[i]]
```

**LeetCode practice:**
- Count Primes (204): https://leetcode.com/problems/count-primes/

---

## Quick Tips / Patterns

- Loop to $\sqrt{n}$ for primality/factorization/divisors.
- Use $\gcd/\operatorname{lcm}$ for array/multiple operations.
- Digit extraction with `% 10` and `// 10` underpins many number problems.
- Precompute primes/factorials for repeated queries.
- Modular arithmetic ($a \bmod m$) is essential for large-number combinatorics.
- Powers: Power of Two (231) — https://leetcode.com/problems/power-of-two/; Power of Three (326) — https://leetcode.com/problems/power-of-three/; Power of Four (342) — https://leetcode.com/problems/power-of-four/