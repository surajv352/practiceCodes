#include<stdio.h>
#define MAX 100
int main()
{
	int sum = 0, count, a[MAX];
	printf("Enter no. of elements: ");
	scanf("%d",&count);
	for (int i = 0; i < count; ++i)
	{
		scanf("%d",&a[i]);
	}
	printf("elements are: ");
	for (int i = 0; i < count; ++i)
	{
		printf("%d ",a[i] );
	}
	for (int i = 0; i < count; ++i)
	{
		sum =  a[i]*a[i];
		printf("\n%d ", sum);
	}
	return 0;
}