with open('sequence.txt', 'r') as f:
    all_numbers = [num.strip() for num in f]

odd = [v for k, v in enumerate(all_numbers) if not k % 2]
even = [v for k, v in enumerate(all_numbers) if k % 2]

odd = [abs(float(x)) for x in odd]
even = [abs(float(x)) for x in even]
a = [abs(float(x)) for x in all_numbers]

average_even = sum(even) / len(even) if even else 0
average_odd = sum(odd) / len(odd) if odd else 0
average_all = sum(a) / len(a) if a else 0

even_k_all = average_even / average_all
odd_k_all = average_odd / average_all


print(f"  │ Четные:   {''.join(['\x1b[48;5;22;1m \x1b[0m' for _ in range(int(even_k_all * 40))]):40s} "
      f"\x1b[48;5;22;1m {even_k_all * 100:.2f}% \x1b[0m │")
print(f"  │ Нечетные: {''.join(['\x1b[48;5;46;1m \x1b[0m' for _ in range(int(odd_k_all * 40))]):40s} "
      f"\x1b[48;5;46;1m {odd_k_all * 100:.2f}% \x1b[0m │")
