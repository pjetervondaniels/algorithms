#include <stdio.h>
int expo(int pot,int base,int expoente,int aux){
	if(aux > expoente){
		return pot;
	}else
		pot = pot*base;
		expo(pot,base,expoente,aux+1);
}


int main (){
	int base,expoente;
	printf("digite a base: ");
	scanf("%d",&base);
	printf("digite o expoente: ");
	scanf("%d",&expoente);
	int aux = 1,pot = 1;
	int potencia = expo(pot,base,expoente,aux);
	printf("%d^%d =  %d",base,expoente,potencia);
	return 0;
}
