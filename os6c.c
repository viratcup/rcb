#include<stdio.h>
#define max 25
void main(){
	int frag[max],b[max],f[max],i,j,nb,nf,temp;
	static int bf[max],ff[max];

	printf("\nMemory Management Scheme - Wrost Fit");
	printf("\nEnter the number of the block : ");
	scanf("%d",&nb);
	printf("Enter the number of the Files : ");
	scanf("%d",&nf);
	printf("Enter the Size of the block : ");

	for(i=1;i<=nb;i++){
	printf("Block %d : ",i);
	scanf("%d",&b[i]);
}
	printf("Enetr the size of the files :- \n");
	
	for(i=1;i<=nf;i++){
	printf("File %d : ",i);
	scanf("%d",&f[i]);
}

	for(i=1;i<=nf;i++){
		temp=1;
		for(j=1;j<=nb;j++){
			if(bf[j]!=1 && b[j]>=temp){
				ff[i]=j;
				frag[i]=b[j];
				bf[j]=1;
				break;
}
}
}

	printf("\nFiles No\tFile Size\tBlock No\tBlock Size\tFragement");
	for(i=1;i<=nf;i++){
		printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d",i,f[i],ff[i],b[ff[i]],frag[i]);

}}





















