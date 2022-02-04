def solution(xs):
    valores = []
    negativos = 0;
    maiorNegativo = -1001
    flagZero = False
    for elem in xs:
        if elem==0:
            flagZero = True
            continue
        if elem<0:
            negativos += 1
            if (elem>maiorNegativo):
                maiorNegativo = elem
        valores.append(elem)
    resto = negativos%2
    if resto!=0 and len(valores)>1:
        valores.remove(maiorNegativo)
    total = 0;
    for i,elem in enumerate(valores):
        if i==0:
            total = elem
        else:
            total = total * elem
    if (total<0 and flagZero==True):
        total = "0"
    return str(total)
