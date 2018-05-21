#Le o arquivo e retorna lista de strings
def leitura_arq():
    #Nome do arquivo a ser aberto
    nome_arq = input('nome do arquivo:')
    #Lista que armazenará o conteúdo do arquivo, cada elemento da lista corresponde a uma linha.
    strings = []
    #Abertura do Arquivo
    arq = open(nome_arq,'r')
    leitura = arq.readlines()
    arq.close()
    aux = ''
    for i in leitura:
        aux += i
    strings = aux.split('(')
    strings2 = []
    for i in strings:
        aux = i.replace(')','')
        strings2.append(aux.split())
    del strings2[0]
    pos = 0
    for l in strings2:
        if(len(l)<1):
            del strings2[pos]
        pos = pos+1

    for u in strings2:
        if(u[0][0] == 'q' and len(u) == 1):
            u.append('()')
        
    return strings2

#Recebe a lista de strings obtida através do arquivo e monta a máquina de moore
def maquina_entrada_moore(strings):
    
    
    '''
        Dicionário que representa a máquina de moore:
    moore = {
            'tipo':'',
            'sim_entrada':[],
            'sim_saida':[],
            'estados':[],
            'inicial':'',
            'finais':[],
            'trans':[][],
            'out':[][]
            }
    '''

    maquina_e['sim_entrada'] = []
    maquina_e['sim_saida'] = []
    maquina_e['estados'] = []
    maquina_e['inicial'] = []
    maquina_e['finais'] = []
    maquina_e['trans'] = []
    maquina_e['out'] = []
    pos = 0
    for y in strings:
        if(y[0] == 'moore'):
            maquina_e['tipo'] = y[0]

        elif(y[0] == 'symbols-in'):
            for c in y:
                if(c != 'symbols-in'):
                    maquina_e['sim_entrada'].append(c)

        elif(y[0] == 'symbols-out'):
            for x in y:
                if(x != 'symbols-out'):
                    maquina_e['sim_saida'].append(x)

        elif(y[0] == 'states'):
            for h in y:
                if(h != 'states'):
                    maquina_e['estados'].append(h)

        elif(y[0] == 'start'):
            maquina_e['inicial'] = y[1]

        elif(y[0] == 'finals'):
            for k in y:
                if(k != 'finals'):
                    maquina_e['finais'].append(k)
            
        elif(y[0] == 'trans' and pos < len(strings)-1):
            aux = pos+1
            while(strings[aux][0][0] == 'q'):
                lst_aux = []
                lst_aux.append(strings[aux][0])
                lst_aux.append(strings[aux][1])
                lst_aux.append(strings[aux][2])
                maquina_e['trans'].append(lst_aux)
                aux = aux+1
                if(aux == len(strings)):
                    break

        elif(y[0] == 'out-fn' and pos < len(strings)-1):
            aux = pos+1
            while(strings[aux][0][0] == 'q'):
                lst_aux = []
                lst_aux.append(strings[aux][0])
                lst_aux.append(strings[aux][1])
                maquina_e['out'].append(lst_aux)
                aux = aux+1
                if(aux == len(strings)):
                    break 

        pos = pos+1    

#Recebe a lista de strings obtida através do arquivo e monta a máquina de mealy
def maquina_entrada_mealy(strings):

    '''Dicionário que representa a máquina de mealy:
    mealy = {
            'tipo':'',
            'sim_entrada':[],
            'sim_saida':[],
            'estados':[],
            'inicial':'',
            'finais':[],
            'trans':[][]
            }

    '''
    
    maquina_e['sim_entrada'] = []
    maquina_e['sim_saida'] = []
    maquina_e['estados'] = []
    maquina_e['inicial'] = []
    maquina_e['finais'] = []
    maquina_e['trans'] = []
    pos = 0
    for y in strings:
        if(y[0] == 'mealy'):
            maquina_e['tipo'] = y[0]

        elif(y[0] == 'symbols-in'):
            for c in y:
                if(c != 'symbols-in'):
                    maquina_e['sim_entrada'].append(c)

        elif(y[0] == 'symbols-out'):
            for x in y:
                if(x != 'symbols-out'):
                    maquina_e['sim_saida'].append(x)

        elif(y[0] == 'states'):
            for h in y:
                if(h != 'states'):
                    maquina_e['estados'].append(h)

        elif(y[0] == 'start'):
            if(len(y)>1):
                maquina_e['inicial'] = y[1]

        elif(y[0] == 'finals'):
            for k in y:
                if(k != 'finals'):
                    maquina_e['finais'].append(k)
            
        elif(y[0] == 'trans' and pos < len(strings)-1):
            aux = pos+1
            while(strings[aux][0][0] == 'q'):
                lst_aux = []
                lst_aux.append(strings[aux][0])
                lst_aux.append(strings[aux][1])
                lst_aux.append(strings[aux][2])
                lst_aux.append(strings[aux][3])
                maquina_e['trans'].append(lst_aux)
                aux = aux+1
                if(aux == len(strings)):
                    break

        pos = pos+1

#Faz a conversão de uma máquina de mealy para uma máquina de moore
def mealy_to_moore():
    maquina_s['tipo'] = 'moore'
    maquina_s['sim_entrada'] = maquina_e['sim_entrada']
    maquina_s['sim_saida'] = maquina_e['sim_saida']
    maquina_s['inicial'] = maquina_e['inicial']
    maquina_s['estados'] = []
    maquina_s['finais'] = []
    maquina_s['trans'] = []
    aux = []
    for i in maquina_e['estados']:
        aux.append([i])

    for i in maquina_e['trans']:
        for y in aux:
            if(i[1] == y[0] and i[3] not in y):
                y.append(i[3])
    pos = 0
    for i in aux:
        if(len(aux[pos]) == 1):
            aux[pos].append('()')
        elif(len(aux[pos]) > 2):
              cont = 0
              str_aux = ''
              for y in aux[pos]:
                  if(cont > 0):
                    aux[pos][0] += str_aux
                    aux.append([aux[pos][0],y])
                    str_aux += '`'
                  cont = cont+1
              del aux[pos]
              continue
        pos = pos+1
        

    maquina_s['out'] = aux
    
    for i in aux:
        maquina_s['estados'].append(i[0])
    
    for i in maquina_e['finais']:
        for y in maquina_s['out']:
            if(i == y[0][:2]):
                maquina_s['finais'].append(y[0])
        
    for i in maquina_e['trans']:
        for y in maquina_s['out']:
            if(i[1] == y[0][:2]):
                if(i[3] == y[1]):
                    maquina_s['trans'].append([i[0],y[0],i[2]])
                    
#Faz a conversão de uma máquina de moore para uma máquina de mealy    
def moore_to_mealy():
    maquina_s['tipo'] = 'mealy'
    maquina_s['sim_entrada'] = maquina_e['sim_entrada']
    maquina_s['sim_saida'] = maquina_e['sim_saida']
    maquina_s['inicial'] = maquina_e['inicial']
    maquina_s['estados'] = []
    maquina_s['finais'] = []
    maquina_s['trans'] = []
    aux = []
    
    for i in maquina_e['estados']:
        if(i[:2] not in maquina_s['estados']):
            maquina_s['estados'].append(i)

    for i in maquina_e['finais']:
        if(i[:2] in maquina_s['estados'] and i[:2] not in maquina_s['finais']):
            maquina_s['finais'].append(i[:2])


    for i in maquina_e['trans']:
        for y in maquina_e['out']:
            if(i[1] == y[0]):
                maquina_s['trans'].append([i[0][:2],i[1][:2],i[2],y[1]])

def verifica_entrada():
    verif = 1
    if(maquina_e['tipo'] != 'mealy' and maquina_e['tipo'] != 'moore'):
        verif = 0
    elif(len(maquina_e['sim_entrada']) == 0):
        verif = 0
    elif(len(maquina_e['sim_saida']) == 0):
        verif = 0
    elif(len(maquina_e['estados']) == 0):
        verif = 0
    elif(len(maquina_e['inicial']) == 0):
        verif = 0
    elif(len(maquina_e['finais']) == 0):
        verif = 0
    elif(len(maquina_e['trans']) == 0):
        verif = 0
    elif(maquina_e['tipo'] == 'moore'):
        if(len(maquina_e['out']) == 0):
            verif = 0
    return verif
    
def escrever_maquina():
    arquivo = open('arq_saida.txt','w')
    arquivo.write('(')
    arquivo.write(maquina_s['tipo'])
    arquivo.write('\n')
    arquivo.write(' (symbols-in')
    for i in maquina_s['sim_entrada']:
        arquivo.write(' ')
        arquivo.write(i)
    arquivo.write(')\n')
    arquivo.write(' (symbols-out')
    for i in maquina_s['sim_saida']:
        arquivo.write(' ')
        arquivo.write(i)
    arquivo.write(')\n')
    arquivo.write(' (states')
    for i in maquina_s['estados']:
        arquivo.write(' ')
        arquivo.write(i)
    arquivo.write(')\n')
    arquivo.write(' (start ')
    arquivo.write(maquina_s['inicial'])
    arquivo.write(')\n')
    arquivo.write(' (finals')
    for i in maquina_s['finais']:
        arquivo.write(' ')
        arquivo.write(i)
    arquivo.write(')\n')
    arquivo.write(' (trans\n')
    arquivo.write(' ')
    cont = 0
    for i in maquina_s['trans']:
        arquivo.write(' (')
        cont2 = 0
        for y in i:
            cont = cont+1
            if(cont2 > 0):
                arquivo.write(' ')
            arquivo.write(y)
            cont2 = cont2+1
        arquivo.write(')')
        if(cont%4 == 0):
            arquivo.write('\n ')
    arquivo.write(')\n')
    if(maquina_s['tipo'] == 'moore'):
        arquivo.write(' (out-fn\n')
        arquivo.write(' ')
        cont = 0
        for i in maquina_s['out']:
            arquivo.write(' (')
            cont2 = 0
            for y in i:
                cont = cont+1
                if(cont2 > 0):
                    arquivo.write(' ')
                arquivo.write(y)
                cont2 = cont2+1
            arquivo.write(')')
            if(cont%5 == 0):
                arquivo.write('\n ')
        arquivo.write(')\n')
    arquivo.write(')')
	arquivo.close()

############### Main ###############        
        
def main():
    import os
    #Leitura do arquivo de entrada
    leitura = leitura_arq()
    aux = ''
    #Maquina Entrada
    global maquina_e
    maquina_e = dict()
    #Maquina Saída
    global maquina_s
    maquina_s = dict()
    if(leitura[0][0] == 'mealy'):
        maquina_entrada_mealy(leitura)
        if(verifica_entrada()):
            mealy_to_moore()
        else:
            print('Erro no arquivo de entrada!')
            return 0
    elif(leitura[0][0] == 'moore'):
        maquina_entrada_moore(leitura)
        if(verifica_entrada()):
            moore_to_mealy()
        else:
            print('Erro no arquivo de entrada!')
            return 0
    else:
        print('Erro no arquivo de entrada!')
        return 0
    for i in maquina_e:
        print(i,': ',maquina_e[i])
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    escrever_maquina()
    print('Máquina de saída escrita em um arquivo "arq_saida.txt"')
    print('--------------------------------------------------------')
    print('--------------------------------------------------------')
    os.system("pause")    
if __name__ == "__main__":
	main()
