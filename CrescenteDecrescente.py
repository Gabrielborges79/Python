X, Y = map(int, input().split())
while ( X != Y     ):
    floor = min(X, Y)
    top = max(X, Y)
    if ( X < Y       ):
        print("Crescente")
    elif (  X > Y      ):
        print("Decrescente")
    X, Y = map(int, input().split())