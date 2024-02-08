#include<stdio.h>
#define max 25
void main(){
	int frag[max],b[max],f[max],i,j,nb,nf,temp,lowest=10000;
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
	for(i=1;i<nf;i++){
		for(j=1;j<=nb;j++){
			if(bf[j]!=1){
				temp=b[j]-f[i];
					if(temp>=0)
						if(lowest>temp){
							ff[i]=j;
							lowest=temp;
}
}
}
	frag[i]=lowest;
	bf[ff[i]]=1;
	lowest=10000;
}

	printf("\nFiles No\tFile Size\tBlock No\tBlock Size\tFragement");
	for(i=1;i<=nf && ff[i]!=0;i++){
		printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d",i,f[i],ff[i],b[ff[i]],frag[i]);
	
}
}
