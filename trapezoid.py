"""Composite trapezoidal rule, Python 3, standard library only."""
import csv
import sys

def trapezoid(f, a, b, n):
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    h = (b - a) / n
    return h * (0.5 * f(a) + sum(f(a + i * h) for i in range(1, n)) + 0.5 * f(b))

if __name__ == "__main__":
    writer = csv.writer(sys.stdout)
    writer.writerow(["n", "h", "estimate", "abs_error"])
    for n in (4, 8, 16):
        estimate = trapezoid(lambda x: x*x, 0.0, 1.0, n)
        writer.writerow([n, 1/n, f"{estimate:.12f}", f"{abs(estimate - 1/3):.12f}"])
