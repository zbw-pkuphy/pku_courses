while True:
    try:
        num = input().strip()
        print("YES" if num == num[::-1] else "NO")
    except EOFError:
        break