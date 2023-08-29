def metragemImovel():
  print('-------------------Menu 1 de 3 Metragem da limpeza-------------------------')
  
  while True:
     metros = input('Digite a metragem do imovel: ')
    
     try:
        metros = float(metros)
        if metros >= 30 and metros < 300:      
           valor = 60 + 0.3 * metros
           print('E necessario contratar uma pessoa.')
           return valor
        elif metros >= 300 and metros < 700:      
            valor = 120 + 0.5 * metros
            print('E necessario contratar duas pessoas.')
            return valor
     except ValueError:
       print('Nao aceitamos metragens abaixo de 30m ou acima de 700m.')  

# inicio da funcao opcao de servico
def opcaoServico():
  print('-------------------Menu 2 de 3 Opcoes de servico---------------------------')
  
  while True:
    opcao = input('Qual a opcao de servico deseja \n' +
                  'b – Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                  'c - Completa - Indicada para sujeiras antigas ou nao rotineiras \n'+
                  '>>> ')
    opcao = opcao.lower()
    opcao = opcao.strip()
    if opcao == 'b':
      multiplicador = 1.00
      return multiplicador
      
    elif opcao == 'c':
      multiplicador = 1.30
      return multiplicador
      
    else:
      print('Opcao invalida') 
      continue 
      

# inicio da funcao servicos extras
def servicoExtra():
  print('-------------------Menu 3 de 3 Servicos extras-----------------------------')
  
  
  acumulador = 0
  while True:
      
           extra = input('Deseja mais algum servico:  \n'+
                  '0 - Não desejo mais nada (encerrar)\n'+
                  '1 - Passar 10 peças de roupas - R$ 10.00 \n'+
                  '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n'+
                  '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n'+
                  '>>> ')     
           if extra == '1':
              acumulador += 10
              
            
           elif extra == '2':
               acumulador += 12
               
           elif extra == '3':
               acumulador += 20
               
           elif extra == '0':
               break
      
           else:
               print('Opcao invalida')
  return acumulador        
  
# programa final
print('--------------Bem vindo ao Guilherme Gallo servicos gerais-----------------')

metros = metragemImovel()
opcao = opcaoServico()
extra = servicoExtra()
total = metros * opcao + extra
print('--------------------------------Total do servico---------------------------')
print('Total do servico: RS{:.2f} (Metragem: {:.2f}, Opcao de servico: {:.2f}, Servico extra: RS{:.2f})'.format(total,metros,opcao,extra))
        