def take(x):
    v_max = max(x)
    v_min = min(x)
    v_sum = sum(x)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")

x = input().split()
f = [int(y) for y in x]
take(f)