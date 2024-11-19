while True :
    cnt = 1
    st = list(input().lower())
    if st == ['#'] :
        break
    print(st[0], st.count(st[0])-1)
