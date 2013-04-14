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
dest = ('localhost', 5000);
udp.sendto ('Conectado com Sucesso', dest);
c = Client();
print 'Aguardando resposta do servidor....';
while True:
	result = c.receiveMinMax(udp);
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