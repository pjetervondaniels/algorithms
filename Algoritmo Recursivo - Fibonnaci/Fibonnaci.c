#include <stdio.h>

int fibonacci(int n){
	if(n<=1){
		return n;
	}
	return fibonacci(n-1)+fibonacci(n-2);
}

int main(){
	int n,result;
	
	printf("\n qual eh o termo da fibonacci:");
	scanf("%d",&n);
	
	result=fibonacci(n);
	
	printf("\n o %d termo de fibonacci eh %d",n,result);
	
	return 0;
}