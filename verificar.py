# Vetor 0 = coringa, 1 = mulher gato, 2 = charada e 3 = hera venenosa  <--- So para lembrar
# Verifica qual candidato tem mais votos e imprime o resultado. 
def verifica_ganhador(candidatos):
    #Usei a porta 'and' e os if/elif para analisar cada candito e ver qual tinha o maior numero de votos 
    if candidatos[0] > candidatos[1] and candidatos[0] > candidatos[2] and candidatos[0] > candidatos[3]:
        print("O ganhador é o Coringa")
    elif candidatos[1] > candidatos[0] and candidatos[1] > candidatos[2] and candidatos[1] > candidatos[3]:
        print("A ganhadora é a Mulher Gato")
    elif candidatos[2] > candidatos[0] and candidatos[2] > candidatos[1] and candidatos[2] > candidatos[3]:
        print("O ganhador é o Charada")
    elif candidatos[3] > candidatos[0] and candidatos[3] > candidatos[1] and candidatos[3] > candidatos[2]:
        print("A ganhadora é a Hera Venenosa")
    else:
        #se der empate ou todos votarem nulo
        print("Gotem vai ser explodida pelas bombas!")