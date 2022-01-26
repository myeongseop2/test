a = input("코로나 접촉자인가(O,X)")

if a == "O":    
    print("PCR해라")
    b = input("열이 나는가?(O,X)")
    if b == "O":
        print("큰일났다 돔항챠~")
    elif b == "X":
        print("다행이네")
elif a == "X":
    print("쉬어라")
