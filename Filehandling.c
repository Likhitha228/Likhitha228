#include<stdio.h>
#include<conio.h>
 int main()
 {
   FILE *fp;
   char ch,fname[30],newch[500];
   int i=0,j,COUNT=0;
   fp=fopen("file.txt","r");
if(!fp)
{
	printf("error in opening the file..\nexiting..");
	getch();
	return 0;
}
printf("\ninput of the reverse funtion: \n");
ch=getc(fp);
while(ch!=EOF)
{
	COUNT++;
	putchar(ch);
	newch[i]=ch;
	i++;
	ch=getc(fp);
}
printf("\n\n\n");
printf("output : \n");
for(j=(COUNT-1);j>=0;j--)
{
	ch=newch[j];
	printf("%c",ch);
}
printf("\n");
getch();
return 0;
}
