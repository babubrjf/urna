eleitor = 1
totalVotos = 0
candA = 0
candB = 0
candC = 0
candD = 0
candE = 0
candF = 0
vBrancos = 0
vNulos = 0
while totalVotos < 30:
  print("=-=-=-=-=-SISTEMA DE VOTAÇÃO CIPA-=-=-=-=-=")
  print("Escolha o número da opção e pressione a tecla ENTER: ")
  print("1 - Candidato A")
  print("2 - Candidato B")
  print("3 - Candidato C")
  print("4 - Candidato D")
  print("5 - Candidato E")
  print("6 - Candidato F")
  print("7 - Voto Branco")
  print("8 - Voto Nulo")
  candNum = int(input())
  if candNum == 1:
    candA = candA + 1
    totalVotos = totalVotos + 1
    eleitor = eleitor + 1
  else:
      if candNum == 2:
        candB = candB + 1
        totalVotos = totalVotos + 1
        eleitor = eleitor + 1
      else:
          if candNum == 3:
            candC = candC + 1
            totalVotos = totalVotos + 1
            eleitor = eleitor + 1
          else:
              if candNum == 4:
                candD = candD + 1
                totalVotos = totalVotos + 1
                eleitor = eleitor + 1
              else:
                  if candNum == 5:
                    candE = candE + 1
                    totalVotos = totalVotos + 1
                    eleitor = eleitor + 1
                  else:
                      if candNum == 6:
                        candF = candF + 1
                        totalVotos = totalVotos + 1
                        eleitor = eleitor + 1
                      else:
                          if candNum == 7:
                            vBrancos = vBrancos + 1
                            totalVotos = totalVotos + 1
                            eleitor = eleitor + 1
                          else:
                              if candNum == 8:
                                vNulos = vNulos + 1
                                totalVotos = totalVotos + 1
                                eleitor = eleitor + 1
      print("Votos totais: " + str(totalVotos))
print("=-=-=-=-=-APURAÇÃO-=-=-=-=-=")
print("Votos Candidato A: " + str(candA))
print("Votos Candidato B: " + str(candB))
print("Votos Candidato C: " + str(candC))
print("Votos Candidato D: " + str(candD))
print("Votos Candidato E: " + str(candE))
print("Votos Candidato F: " + str(candF))
print("Votos Brancos: " + str(vBrancos))
print("Votos Nulos: " + str(vNulos))
print("Votos Totais: " + str(totalVotos))
print("Não votantes: " + str(70 - totalVotos))