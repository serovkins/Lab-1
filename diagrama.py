with open('sequence.txt', 'r') as f:
    all_numbers = [num.strip() for num in f]

nechet = [v for k, v in enumerate(all_numbers) if not k % 2]
chet = [v for k, v in enumerate(all_numbers) if k % 2]

nechet = [abs(float(x)) for x in nechet]
chet = [abs(float(x)) for x in chet]
a = [abs(float(x)) for x in all_numbers]

average_chet = sum(chet) / len(chet) if chet else 0
average_nechet = sum(nechet) / len(nechet) if nechet else 0
average_all = sum(a) / len(a) if a else 0

otnoshenie_chet_k_all = average_chet / average_all
otnoshenie_nechet_k_all = average_nechet / average_all


print(f"  │ Четные:   {''.join(['\x1b[48;5;22;1m \x1b[0m' for _ in range(int(otnoshenie_chet_k_all * 40))]):40s} "
      f"\x1b[48;5;22;1m {otnoshenie_chet_k_all * 100:.2f}% \x1b[0m │")
print(f"  │ Нечетные: {''.join(['\x1b[48;5;46;1m \x1b[0m' for _ in range(int(otnoshenie_nechet_k_all * 40))]):40s} "
      f"\x1b[48;5;46;1m {otnoshenie_nechet_k_all * 100:.2f}% \x1b[0m │")