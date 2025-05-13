while True:
    n = int(input("Input banyak data n: "))
    data = []
    for i in range(n):
        x = float(input(f"Input x ke {i+1}: "))
        if x > 0:
            fx = 4*x**3 + 7*x - 5
        elif x < 0:
            fx = 3*x**2 - 5*x + 1
        else:  # x == 0
            fx = 4*x**3 + 7*x - 5 

        gx = fx**2 - fx
        hx = fx * gx
        
        data.append([i+1, x, fx, gx, hx])
    

    print("| No | x     | f(x)      | g(x)      | h(x)      |")
    print("|----|-------|-----------|-----------|-----------|")
    for z in range(len(data)):
        print(f"| {data[z][0]:2} | {data[z][1]:5.2f} | {data[z][2]:8.2f} | {data[z][3]:8.2f} | {data[z][4]:8.2f} |")
    
    jawaban = input("\nInput nilai x lagi? (ketik 'tidak' untuk berhenti): ")
    if jawaban == "tidak":
        break