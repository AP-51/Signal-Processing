#include<stdio.h>
#include<stdlib.h>
int main()
{
	int i;
	int k=20;
	FILE *fp;
	fp=fopen("de.dat","w");
	double x[6]={1.0,2.0,3.0,4.0,2.0,1.0},y[20];
	y[0]=x[0];
	y[1]=-0.5*y[0]+x[1];
	fprintf(fp, "%lf\n%lf\n", y[0],y[1]);
	for(i=2;i<k;i++)
	{
		if(i<6) y[i]= -0.5*y[i-1]+x[i]+x[i-2];
		else if((i>5)&&(i<8)) y[i] = -0.5*y[i-1]+x[i-2];
		else y[i] = -0.5*y[i-1];
		fprintf(fp, "%lf\n", y[i]);
	}
	fclose(fp);
	return 0;
}



