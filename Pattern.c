#include<stdio.h>
int main()
{
	int n,i,j,s=0,pattern=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		s=n-(i+1);
		for(j=0;j<s;j++)
		{
			printf(" ");
		}
		pattern=i+1;
		for(j=0;j<pattern;j++)
		{
			printf("01");
		}
		printf("\n");
	}
}

Output
6
     01
    0101
   010101
  01010101
 0101010101
010101010101
