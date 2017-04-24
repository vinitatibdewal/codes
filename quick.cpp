#include<iostream>
#include<omp.h>
#include<stdlib.h>
using namespace std;

void swap(int *a,int i,int j)
{
	int temp=a[i];
	a[i]=a[j];
	a[j]=temp;
}

int part(int *a,int l,int h)
{
	int x=a[h];	//pivot
	int i=l-1,j;
	for(j=l;j<=h-1;j++)
	{
		if(a[j]<=x)
		{
		i=i+1;
		swap(a,i,j);	
		}
	}
	swap(a,i+1,h);
	return i+1;
}
void quick(int *a,int l,int h)
{
	if(l<h)
	{
		int p=part(a,l,h);
		#pragma omp parallel sections
		{
		#pragma omp parallel section
		{
			quick(a,p+1,h);
		}
		#pragma omp parallel section
		{
			quick(a,l,p-1);
		}
		}
	}
}

void disp(int *a,int n)
{	
	cout<<"Sorted Array:\n";
	for(int i=0;i<n;i++)
	{
		cout<<"\t"<<a[i];
	}
}

int main(int arg,char **argc)
{
string str2,str1="";
int max=0;
str2=argc[1];
int a[20];
for(int i=0;i<str2.size();i++)
{
if(str2[i]!=',')
	str1=str1+str2[i];
else
{
	a[max]=atoi(str1.c_str());
	max+=1;
	str1="";
}
if(i==str2.size()-1)
{
	a[max]=atoi(str1.c_str());
	max=max+1;
}		
}
quick(a,0,max-1);
disp(a,max);
}
