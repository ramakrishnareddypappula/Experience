
# Many algorithms are present which have pros and cons.

# Knuth-Morris-Pratt (KMP): Used when patterns contain repeated sub patterns. It uses partial matching to skip pattern when there is no match.
# Boyer-Moore : It uses bad char and good suffix rule to skip sections quickly.
# Rabin-Karp : This uses rolling hash to compare pattern with the text. Good for searching patterns long text but not good for patterns with distinct chars.

    # Rabin karp calculates hash value using hash function for a pattern and compares it with text.
    # Hash function maps chars to a hash value. A collision will occur when 2 different input texts will have same hash value.
    # example : if a = 1 , b = 2.. z = 26
                # "ad" = 1 + 4 = 5 , bc = 2 + 3 = 5
                # hash value is same for 2 different strings. This is collision.
                # This can be mitigated by using prime number as modulus.


def RabinKarp(text, pattern):
    n = len(text)
    m = len(pattern)
    d = 256
    q = 101
    h = 1
    p = 0
    t = 0
    result = []

    # Pre-processing
    for i in range(m-1):
        h = (h*d)%q

    # Calculating the hash value of the pattern
    for i in range(m):
        p = (d*p + ord(pattern[i]))%q
        t = (d*t + ord(text[i]))%q

    # Rolling hash
    for i in range(n-m+1):
        if p == t:
            match = True
            for j in range(m):
                if pattern[j] != text[i+j]:
                    match = False
                    break
            if match:
                result.append(i)

        if i < n-m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m]))%q
            if t < 0:
                t = t+q

    return result

# Example usage
text = "This is a sample text to demonstrate the Rabin-Karp algorithm."
pattern = "text"
print(RabinKarp(text, pattern))



