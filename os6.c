#include<stdio.h>
#define max 25
void main(){
	int frag[max],b[max],f[max],bf[max],ff[max],i,j,nb,nf,temp;
	for(i=0;i<max;i++){
		frag[i]=0;
		bf[i]=0;
		ff[i]=0;
}

	printf("\n\t Memory Management Scheme - Wrost Fit");
	printf("\nEnter the number of the block : ");
	scanf("%d",&nb);
	printf("Enter the number of the Files : ");
	scanf("%d",&nf);
	printf("Enter the Size of the block : ");

	for(i=1;i<=nb;i++){
	printf("Block %d",i);
	scanf("%d",&b[i]);
}
	printf("Enetr the size of the files :- \n");
	
	for(i=1;i<=nf;i++){
	printf("File %d",i);
	scanf("%d",&f[i]);
}

	for(i=1;i<=nf;i++){
		for(j=1;i<=nb;j++){
			if(bf[j]!=1){
				temp=b[j]-f[i];
				if(temp>=0){
					ff[i]=j;
					break;			
}
}

}
	frag[i]=b[ff[i]]-f[i];
	bf[ff[i]]=1;
	
	printf("\nFile_no.:\tFile_size:\tBlock_no:\tBlock_size:\tFragement");
	for(i=1;i<=nf;i++){
		printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d",i,f[i],ff[i],b[ff[i]],frag[i]);




}}

}
