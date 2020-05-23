#include <stdio.h>

int fatorial(int n){
	if(n==1){
		return 1;
	}
	if(n!=1){
		return n*fatorial(n-1);
	}
	
}

int main(){
	int n,result;
	
	printf("\n qual eh o ultimo termo da fatorial:");
	scanf("%d",&n);
	
	result=fatorial(n);
	
	printf("\n o fatorial eh %d",result);
	
	return 0;
}