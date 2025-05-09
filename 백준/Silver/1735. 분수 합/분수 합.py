denom1 = list(map(int, input().split()))
denom2 = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)

common_denominator = lcm(denom1[1], denom2[1])

numerator1 = denom1[0] * (common_denominator // denom1[1])
numerator2 = denom2[0] * (common_denominator // denom2[1])

total_numerator = numerator1 + numerator2

gcd_value = gcd(total_numerator, common_denominator)

print(total_numerator // gcd_value, common_denominator // gcd_value)