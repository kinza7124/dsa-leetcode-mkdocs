# Mathematics Fundamentals for DSA

An **intuition-first** reference for core mathematics concepts used in **Data Structures & Algorithms** and **LeetCode-style problems**.
This file focuses on **how and why things work**, not shortcuts or heavy optimizations.

---

## 1. Divisors of a Number

### What is a divisor?

A number `d` is a **divisor** of `n` if it divides `n` completely.

Mathematically:

```
n % d == 0
```

### Intuition

Divisors always come in **pairs**.
If `d` divides `n`, then `n / d` also divides `n`.

Example for `n = 36`:

* `1 × 36`
* `2 × 18`
* `3 × 12`
* `4 × 9`
* `6 × 6`

Once `d > √n`, pairs start repeating.
So we only check until `√n`.

### Basic Algorithm (Intuitive)

```cpp
for (int i = 1; i * i <= N; i++) {
    if (N % i == 0) {
        // i is a divisor
        // N / i is also a divisor
    }
}
```

### Applications

* Counting divisors
* Checking prime numbers
* Factorization problems

---

## 2. Prime Numbers

### Definition

A **prime number** has **exactly two divisors**:

* `1`
* the number itself

Examples:

* Prime: `2, 3, 5, 7, 11`
* Not prime: `4 (1,2,4)`, `6 (1,2,3,6)`

### Intuition

If a number has **any divisor other than 1 and itself**, it is not prime.

Because divisors come in pairs, we only need to check until `√n`.

### Naive Prime Check (Understanding First)

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    int cnt = 0;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            cnt++;
            if (i != n / i) cnt++;
        }
    }
    return cnt == 2;
}
```

---

## 3. Prime Factorization

### What is it?

Breaking a number into **only prime numbers** whose product equals the number.

Example:

```
60 = 2 × 2 × 3 × 5
```

### Intuition

* Try dividing by the smallest possible number
* Keep dividing while divisible
* Whatever remains at the end is prime

### Basic Factorization Pattern

```cpp
for (int i = 2; i * i <= n; i++) {
    while (n % i == 0) {
        // i is a prime factor
        n =n/i;
    }
}
if (n > 1) {
    // n itself is a prime factor
}
```

---

## 4. Greatest Common Divisor (GCD)

### Meaning

The **largest number** that divides both `a` and `b`.

Example:

```
gcd(12, 18) = 6
```

### Euclid’s Algorithm – Intuition

If `a` divides `b`, then:

```
gcd(a, b) = gcd(b, a % b)
```

We keep shrinking the problem until remainder becomes `0`.

### Code

```cpp
int gcd(int a, int b) {
    while (b>0 && a>0) {
        if(a>b)
        a = a % b;
        
        if(b>a)
        b=b%a;
    }
    if(a==0)
    return b;
return a;
}
```

---

## 5. Least Common Multiple (LCM)

### Meaning

The **smallest number** divisible by both `a` and `b`.

### Key Relation

```
LCM(a, b) = a×b/GCD(a, b) 
```

### Code

```cpp
int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;
}
```

---

## 6. Important Sum Formulas

Used heavily in missing-number and counting problems.

* Sum of first `n` numbers:

```
n(n + 1) / 2
```

* Sum of squares:

```
n(n + 1)(2n + 1) / 6
```

* Sum of cubes:

```
(n(n + 1) / 2)^2
```

---

## 7. Missing Number Problems

### Problem Pattern

Given numbers from `0` to `n` with **one missing**, find it.

### Intuition

We know what the sum *should* be.
We subtract what we *actually* have.

### Code

```cpp
int missingNumber(vector<int>& nums) {
    int n = nums.size();
    int expected = n * (n + 1) / 2;
    int sum = 0;
    for (int x : nums)
        sum += x;
    return expected - sum;
}
```

---

## 8. Digit Extraction (MOST IMPORTANT PATTERN)

### Core Idea

For any number `n`:

* Last digit → `n % 10`
* Remove digit → `n / 10`

### Universal Digit Loop

```cpp
while (n > 0) {
    int digit = n % 10;
    n = n/10;
}
```

This single loop powers:

* Sum of digits
* Reverse number
* Palindrome
* Armstrong
* Happy number

---

## 9. Reverse a Number

### Intuition

Extract digits and rebuild the number from left to right.

```cpp
int reverse(int n) {
    int rev = 0;
    while (n > 0) {
        int digit = n%10;
        rev = rev * 10 + digit;
        n = n/10;
    }
    return rev;
}
```

---

## 10. Palindrome Number

### Idea

A number is palindrome if:

```
original == reverse(original)
```

```cpp
bool isPalindrome(int n) {
    if (n < 0) return false;
    int original = n, rev = 0;
    while (n > 0) {
        int digit = n%10;
        rev = rev * 10 + digit;
        n = n/10;
    }
    return original == rev;
}
```

---

## 11. Armstrong Number

### Definition

A number is Armstrong if:

```
(sum of each digit ^ number of digits) == number
```

### Intuition

* First count digits
* Then raise each digit to that power
* Add and compare

```cpp
bool isArmstrong(int n) {
    int temp = n, count = 0;
    while (temp > 0) {
        count++;
        temp = temp/10;
    }

    int sum = 0;
    temp = n;
    while (temp > 0) {
        int digit = temp % 10;
        sum += pow(digit, count);
        temp /= 10;
    }
    return sum == n;
}
```

---

## 12. Happy Number

### Idea

Repeatedly replace number with:

```
sum of squares of digits
```

If it becomes `1` → Happy
If it repeats → Cycle → Not Happy

### Why a set?

To detect infinite loops.

```cpp
int extractDigits(int n) {
    int sum = 0;
    while (n > 0) {
        int d = n % 10;
        sum += d * d;
        n = n/10;
    }
    return sum;
}

bool isHappy(int n) {
    unordered_set<int> seen;
    while (n != 1) {
        if (seen.count(n)) return false;
        seen.insert(n);
        n = extractDigits(n);
    }
    return true;
}
```

---

## 13. Sieve of Eratosthenes

### Intuition

Instead of checking each number:

* Assume all are prime
* Remove multiples of each prime

```cpp
void sieve(int N) {
    vector<bool> prime(N + 1, true);
    prime[0] = prime[1] = false;

    for (int i = 2; i * i <= N; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= N; j += i)
                prime[j] = false;
        }
    }
}
```

---

## 14. Arrange Coins (Binary Search Intuition)

### Problem Insight

To form `k` rows:

```
coins needed = k(k + 1) / 2
```

Find the **maximum k** such that this ≤ `n`.

```cpp
int arrangeCoins(int n) {
    long long left = 0, right = n;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        long long curr = mid * (mid + 1) / 2;
        if (curr == n) return mid;
        if (curr < n) left = mid + 1;
        else right = mid - 1;
    }
    return right;
}
```

---

## 🔑 Final Patterns to Remember

* `% 10` and `/ 10` unlock digit problems
* Divisors always come in pairs
* Loop until `√n`, not `n`
* GCD + LCM appear everywhere
* Mathematical formulas save loops

Master these and **DSA math becomes easy** 🚀
