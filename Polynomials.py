def poly_str(p: list):
    n = len(p)
    coeffs = p[::-1]
    i = 0
    result = ''
    while i < n:
        c = coeffs[i]
        a = '' if abs(c) == 1 else abs(c)
        d = n - i - 1
        # Zero coefficients
        if c == 0:
            if n == 1:
                term = '0'
            else:
                term = ''
        else:
            # The sign depends on the coefficient and the degree
            if d == n - 1:
                sign = '-' if c < 0 else ''
            else:
                sign = '+' if c > 0 else '-'
            # The exponent depends on the degree
            if d == 0:
                if n == 1:
                    term = str(c)
                else:
                    term = ('+' if c > 0 else '') + str(c)
            elif d == 1:
                term = sign + str(a) + 'X'
            else:
                term = sign + str(a) + 'X^' + str(d)
        result += term
        i += 1
    return result


def poly_degree(p: list):
    return len(p) - 1


def poly_add(p: list, q: list):
    m = max(len(p), len(q))
    r = [0] * m
    for i in range(m):
        a = p[i] if i < len(p) else 0
        b = q[i] if i < len(q) else 0
        r[i] += a + b
    return r


def poly_scalar(p: list, a: int):
    m = len(p)
    for i in range(m):
        p[i] *= a
    return p


def poly_prod(p: list, q: list):
    m = poly_degree(p)
    n = poly_degree(q)
    o = m + n
    r = [0] * (o + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            k = i + j
            r[k] += p[i] * q[j]
    return r


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


def poly_derive(p: list, m: int):
    n = len(p)
    o = n - m if n - m > 0 else 1
    q = [0] * o
    for i in range(o):
        j = min(i + m, n - 1)
        f = fact(j) // fact(i) if m < n else 0
        q[i] = p[j] * f
    return q


# Calculations

p0 = [0]
p1 = [-1, 4, -7, 2]
p2 = [1, 0, 0, 2]
p3 = [3, 0, -1, 1]
p4 = [0, -2, 3, 0, -1]

print('Printing polynomials:')
print(p0, '-->', poly_str(p0))
print(p1, '-->', poly_str(p1))
print(p2, '-->', poly_str(p2))
print(p3, '-->', poly_str(p3))
print(p4, '-->', poly_str(p4), end='\n\n')

print('Calculating degrees:')
print(p0, '-->', poly_degree(p0))
print(p1, '-->', poly_degree(p1))
print(p2, '-->', poly_degree(p2))
print(p3, '-->', poly_degree(p3))
print(p4, '-->', poly_degree(p4), end='\n\n')

print('Adding polynomials:')
print(poly_str(p1), ' + ', poly_str(p2), '-->', poly_str(poly_add(p1, p2)))
print(poly_str(p1), ' + ', poly_str(p3), '-->', poly_str(poly_add(p1, p3)))
print(poly_str(p2), ' + ', poly_str(p3), '-->', poly_str(poly_add(p2, p3)))
print(poly_str(p3), ' + ', poly_str(p4), '-->', poly_str(poly_add(p3, p4)), end='\n\n')

print('Product by a scalar:')
print(poly_str(p1), ' x ', 2, '-->', poly_str(poly_scalar(p1, 2)))
print(poly_str(p2), ' x ', -3, '-->', poly_str(poly_scalar(p2, -3)))
print(poly_str(p3), ' x ', 7, '-->', poly_str(poly_scalar(p3, 7)), end='\n\n')

print('Product of polynomials:')
print(poly_str(p1), ' x ', poly_str(p2), '-->', poly_str(poly_prod(p1, p2)))
print(poly_str(p1), ' x ', poly_str(p3), '-->', poly_str(poly_prod(p1, p3)))
print(poly_str(p2), ' x ', poly_str(p3), '-->', poly_str(poly_prod(p2, p3)))
print(poly_str(p3), ' x ', poly_str(p4), '-->', poly_str(poly_prod(p3, p4)), end='\n\n')

print('Deriving polynomials:')
print(str(0) + 'th derived of', poly_str(p1), '-->', poly_str(poly_derive(p1, 0)))
print(str(1) + 'th derived of', poly_str(p1), '-->', poly_str(poly_derive(p1, 1)))
print(str(2) + 'th derived of', poly_str(p1), '-->', poly_str(poly_derive(p1, 2)))
print(str(3) + 'th derived of', poly_str(p1), '-->', poly_str(poly_derive(p1, 3)))
print(str(4) + 'th derived of', poly_str(p1), '-->', poly_str(poly_derive(p1, 4)), end='\n\n')
