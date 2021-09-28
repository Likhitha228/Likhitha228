#include<stdio.h>
struct employee
{
	int age,salary,phonenumber;
	char name[25];
}emp[100];
void main()
{
	int i,n;
	printf("enter no of employees\n");
	scanf("%d",&n);
	printf("enter employee info as name,age,phone number,salary\n");
	for(i=0;i<n;i++)
	{
		scanf("%s %d %d %d",emp[i].name,&emp[i].age,&emp[i].phonenumber,&emp[i].salary);
    }
    printf("\nname\tage\tphone number\tsalary\n");
    for(i=0;i<n;i++)
    {
    	printf("%s\t%d\t%d\t%d\n",emp[i].name,emp[i].age,emp[i].phonenumber,emp[i].salary);
	}
}
