#Professor passou esse trabalho com o tema e falou que 20 pessoas iam votar
from verificar import verifica_ganhador 
def votacao():
    candidatos = [0, 0, 0, 0]  # Vetor 0 = Coringa, 1 = Mulher Gato, 2 = Charada, 3 = Hera Venenosa

    for i in range(20):
        quem = input("-Digite 1 para votar no Coringa \n-Digite 2 para votar na Mulher Gato \n-Digite 3 para votar Charada\n-Digite 4 Para votar na Hera venenosa \n-se número >= 5 o voto é nulo \n-Vote:  ")
        match quem:
            case "1":
                candidatos[0] += 1
            case "2":
                candidatos[1] += 1
            case "3":
                candidatos[2] += 1
            case "4":
                candidatos[3] += 1
    
    verifica_ganhador(candidatos)

votacao()