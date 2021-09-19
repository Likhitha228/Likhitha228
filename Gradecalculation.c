#include<stdio.h>
int main()
{
	int mark;
	printf("Enter a number:");
	scanf("%d",&mark);
	if(mark>84&&mark<=100)
	{
		printf("A Grade");
	}
	else if(mark>69&&mark<=84)
	{
		printf("B Grade");
	}
	else if(mark>54&&mark<=69)
	{
		printf("C Grade");
	}
	else if(mark>39&&mark<=54)
	{
		printf("D Grade");
	}
	else if(mark>=0&&mark<40)
	{
		printf("F Grade");
	}
	else
	{
		printf("Invalid Mark");
	}
	return 0;
}

Output
Enter a number:92
A Grade
Enter a number:77
B Grade
Enter a number:68
C Grade
Enter a number:53
D Grade
Enter a number:35
F Grade
