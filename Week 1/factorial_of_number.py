
# Sonning Faktorialini topadigan dastur

n = int(input("\nSonni kiriting: "))

result = 1

for i in range(1, n+1):
    result *= i

print(f"{n} sonining faktoriali {result}")

# endi to'g'ri bo'ldi