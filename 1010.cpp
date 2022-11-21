#include<stdio.h>
int main()
{
	char a[96];
	int j = 0;
	while(a[j]!='\n')
	{
		scanf("%c",&a[j]);
		j++;
		printf("%c",a[j]);
	}

	
	int i = 0,letter = 0,blank = 0,digit = 0,other = 0;
	for(;i<j;i++)
	{
		if((a[i]>='A'&&a[i]<='Z')||(a[i]>='a'&&a[i]<='z'))
		letter++;
		else if(a[i]==' '||a[i]=='\n')
		blank++;
        else if(a[i]>='0'&&a[i]<='9')
        digit++;
        else
        other++;
	}
	
	printf("%d\n%d\n%d\n%d\n",letter,blank,digit,other);
	
	return 0;
}

