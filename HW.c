#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *fpr;
	int *ftr;
	ftr = (int*) malloc(100*sizeof(int));
	fpr = fopen("data.txt", "r");

	int sum = 0;	
	
	if (fpr == NULL)
	{
		printf("Memory cannot be allocated");
		exit(0);
	}

	while(fscanf(fpr, "%d", ftr) !=EOF)
	{
		sum = sum + *ftr;
	}
	printf("%d\n is the sum", sum);
	
	fclose(fpr);
	free(ftr);
	fpr = fopen("result.txt", "w+");
	fprintf(fpr, "%d\n", sum);

	fclose(fpr);
}
