#include<stdio.h>
main()
{
	printf("pick an item: \n1. pizza\n2. burger\n3. pasta\n4. french fries\n5. sandwich");
	int choice=0;
	scanf("%d",&choice);
	switch(choice)
	{
		case 1:
			printf("Food item-pizza\n");
			printf("Prize-Rs 239\n");
			break;
		case 2:
		    printf("Food item-burger\n");
			printf("Prize-Rs 129\n");
			break;
		case 3:
		    printf("Food item-pasta\n");
			printf("Prize- Rs 179\n");
			break;
		case 4:
		    printf("Food item-french fries\n");
			printf("Prize- Rs 99");
			break;
		case 5:
		    printf("Food item- sandwich\n");
			printf("prize- Rs 149");
			break;
		default : printf("use the default case");					
	}
}
