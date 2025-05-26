import math

# === BASIC MATH FUNCTIONS ===
print("== BASIC MATH FUNCTIONS ==")
print("ceil(4.3):", math.ceil(4.3))
print("floor(4.7):", math.floor(4.7))
print("trunc(4.9):", math.trunc(4.9))
print("fabs(-5):", math.fabs(-5))
print("factorial(5):", math.factorial(5))
print("fmod(10.5, 3):", math.fmod(10.5, 3))
print("remainder(10, 3):", math.remainder(10, 3))
print("modf(5.75):", math.modf(5.75))

# === POWER & LOGARITHMS ===
print("\n== POWER & LOGARITHMS ==")
print("pow(2, 3):", math.pow(2, 3))
print("sqrt(16):", math.sqrt(16))
print("exp(2):", math.exp(2))
print("expm1(1e-5):", math.expm1(1e-5))
print("log(10):", math.log(10))
print("log10(100):", math.log10(100))
print("log2(8):", math.log2(8))
print("log1p(1e-5):", math.log1p(1e-5))

# === TRIGONOMETRY ===
print("\n== TRIGONOMETRY ==")
print("sin(pi/2):", math.sin(math.pi / 2))
print("cos(0):", math.cos(0))
print("tan(pi/4):", math.tan(math.pi / 4))
print("asin(1):", math.asin(1))
print("acos(0):", math.acos(0))
print("atan(1):", math.atan(1))
print("atan2(1, 1):", math.atan2(1, 1))

# === HYPERBOLIC FUNCTIONS ===
print("\n== HYPERBOLIC FUNCTIONS ==")
print("sinh(1):", math.sinh(1))
print("cosh(1):", math.cosh(1))
print("tanh(1):", math.tanh(1))
print("asinh(1):", math.asinh(1))
print("acosh(2):", math.acosh(2))
print("atanh(0.5):", math.atanh(0.5))

# === CONVERSIONS & SPECIAL FUNCTIONS ===
print("\n== CONVERSIONS & SPECIAL FUNCTIONS ==")
print("radians(180):", math.radians(180))
print("degrees(pi):", math.degrees(math.pi))
print("isfinite(10):", math.isfinite(10))
print("isinf(math.inf):", math.isinf(math.inf))
print("isnan(math.nan):", math.isnan(math.nan))
print("copysign(5, -3):", math.copysign(5, -3))
print("fsum([0.1, 0.2, 0.3]):", math.fsum([0.1, 0.2, 0.3]))
print("prod([2, 3, 4]):", math.prod([2, 3, 4]))
print("dist([0, 0], [3, 4]):", math.dist([0, 0], [3, 4]))
print("hypot(3, 4):", math.hypot(3, 4))
print("isclose(0.1 + 0.2, 0.3):", math.isclose(0.1 + 0.2, 0.3))
print("nextafter(1.0, 2.0):", math.nextafter(1.0, 2.0))
print("ulp(1.0):", math.ulp(1.0))

# === CONSTANTS ===
print("\n== CONSTANTS ==")
print("pi:", math.pi)
print("e:", math.e)
print("tau:", math.tau)
print("inf:", math.inf)
print("nan:", math.nan)
