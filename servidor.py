# coding: latin-1
import socket
import math

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
orig = ('localhost', 5000);
udp.bind(orig);

print 'Programa Somador de 0 ate N - Utilizando Balanceamento de Carga\n\n';

print 'Digite a quantidade de clientes que sao esperados:\n';
nProcessors = int(raw_input());

print 'Aguardando ',nProcessors,' clientes';
conected = 0;
listClients = [];
while conected < int(nProcessors):
    message, adressClient = udp.recvfrom(1024);
    listClients.insert(conected,adressClient);
    conected = conected + 1;
    
print 'Clientes conectados com sucesso.';
print 'Entre com o numero a ser feito o seu somatorio\n';
number = raw_input();
number = int(number);
#number = 4000;

pieces = 13;
vectStart = [];
vectEnd = [];
sumAux = 0;
sumFinal = 0;
part = number / pieces;
for i in range(0,pieces):
	vectStart.insert(i, i * part + 1);
	vectEnd.insert(i,(i + 1) * part);
	if(i == ( pieces - 1) and vectEnd[i] != number):
		vectEnd[i] = number;

sent = 0;
for i in range(0,nProcessors):
	udp.sendto (str(vectStart[sent]), listClients[i]);
	udp.sendto (str(vectEnd[sent]), listClients[i]);
	sent = sent + 1;

while sent <= pieces -1:
	sumAux, addressServer = udp.recvfrom(1024);
	sumFinal = sumFinal + int(sumAux);
	udp.sendto (str(vectStart[sent]),addressServer);
	udp.sendto (str(vectEnd[sent]), addressServer);
	sent = sent + 1;

for i in range(0,nProcessors):
	sumAux, addressServer = udp.recvfrom(1024);
	udp.sendto (str(-1),addressServer);
	sumFinal = sumFinal + int(sumAux);


print 'Resultado da operacao:',sumFinal;
# MESTRE
# ======
# Inicio
# int pedacos = numpedacos();
# int vetinic[pedacos], vetfim[pedacos];
# int valor, parte;
# int somapar=0;
# leia(valor);
# parte=valor/pedacos;
# Para i=0 até pedacos-1 faça
#    vetinic[i]=i*parte+1;
# vetfim[i]=(i+1)*parte;
# se(i==pedacos-1 e vetfim[i]!=valor) então
#      vetfim[i]=valor;
#    fimse
# FimPara
# foi=0;
# Para i=1 até N-1 faça
#   envie vetinic[foi] para processador i; 
# envie vetfim[foi] para processador i;
# foi=foi+1;
# FimPara
# Enquanto foi <= pedacos-1 faça
#   receba somaesc de algum processador;
# id=id do processador do qual acabou de chegar a mensagem;
# somapar=somapar+somaesc;
# envie vetinic[foi] para processador id; 
# envie vetfim[foi] para processador id;
# foi=foi+1;
# FimEnquanto  
# Para i=1 até N-1 faça
#    receba somaesc de processador i;
#    somapar=somapar+somaesc;
# Fim Para
# Escreva somapar;
    
# Fim