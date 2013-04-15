# coding: latin-1
import socket
class Client(object):
	min,max,sum = 0,0,0;

	def sendSum(self,udp,dest	):
		udp.sendto (str(self.sum), dest);

	def receiveMinMax(self,udp):
		self.min, addressServer = udp.recvfrom(1024);
		self.min = int(self.min);
		if(self.min < 0):
			return False;
		self.max, addressServer = udp.recvfrom(1024);
		
		self.max = int(self.max);
		return True;

	def doSum(self):
		self.sum = 0;
		for i in range(self.min,self.max+1):
			self.sum = self.sum + i;
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
print 'Entre com o Endereco do Servidor:';
HOST = raw_input();

print 'porta:';
PORT = int(raw_input());


dest = (HOST, PORT);
udp.sendto ('Conectado com Sucesso', dest);
c = Client();
print 'Aguardando outros conectarem ao servidor do servidor....';
flagMensagem = 0;
while True:
	result = c.receiveMinMax(udp);
	if(flagMensagem == 0):
		print 'Conectado com sucesso.';
		flagMensagem = 1;
	if(result == False):
		break;
	c.doSum();
	c.sendSum(udp,dest);


print 'Cargas esgotadas...Programa encerrado.';

# Inicio
#   int somaesc=0;
#   receba inic do processador 0;
# 	receba fim do processador 0;
# 	somaesc=soma(inic, fim);
# 	envie somaesc para processador 0;
# Fim