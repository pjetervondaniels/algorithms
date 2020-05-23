#include <stdio.h>

int somatorio(int n){
	if(n==1){
		return 1;
	}
	if(n!=1){
		return n+somatorio(n-1);
	}
	
}

int main(){
	int n,result;
	printf("\n qual eh o ultimo termo do somatorio?");
	scanf("%d",&n);
	
	result=somatorio(n);
	
	printf("\n o somatorio eh %d",result);
	
	return 0;
}