n, m = map(int, input().split())

board = [input() for _ in range(n)]

min_repaint = float('inf')

for x in range(n - 7):
    for y in range(m - 7):
        count_w = 0
        for i in range(8):
            for j in range(8):
                current_color = board[x + i][y + j]
                expected_color = 'W' if (i + j) % 2 == 0 else 'B'
                if current_color != expected_color:
                    count_w += 1
        
        count_b = 0
        for i in range(8):
            for j in range(8):
                current_color = board[x + i][y + j]
                expected_color = 'B' if (i + j) % 2 == 0 else 'W'
                if current_color != expected_color:
                    count_b += 1
        
        min_repaint = min(min_repaint, count_w, count_b)

print(min_repaint)
