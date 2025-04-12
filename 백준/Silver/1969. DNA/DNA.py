n, m = map(int, input().split())

dna_list = [input() for _ in range(n)]

answer = ''
total_hamming_distance = 0
nucleotide = ['A', 'C', 'G', 'T']

for i in range(m):
    dna_cnt = [0] * 4
    for dna in dna_list:
        dna_cnt[nucleotide.index(dna[i])] += 1

    max_cnt = max(dna_cnt)
    max_idx = dna_cnt.index(max_cnt)
    answer += nucleotide[max_idx]
    total_hamming_distance += (n - max_cnt)

print(answer)
print(total_hamming_distance)