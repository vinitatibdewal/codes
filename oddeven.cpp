#include <iostream>
#include<omp.h>
#include <stdlib.h>
using namespace std;
void swap(int *,int *);
void oddeven_sort(int *,int);
int main(int arg,char **argv)
{  
	string str2,str1="";	//Same as quicksort
	int max=0;
	str2=argv[1];
	int arr[20];
	for(int i=0;i<str2.size();i++)
	{
		if(str2[i]!=',')
		str1=str1+str2[i];
		else
		{
			arr[max]=atoi(str1.c_str());
			max+=1;
			str1="";
		}
		if(i==str2.size()-1)
		{
			arr[max]=atoi(str1.c_str());
			max=max+1;
		}
	}
	cout<<"\n sorted elements are: ";
	oddeven_sort(arr,max);
    	for (int i = 0;i < max;i++)
      		cout<<"\t"<<arr[i];
}
/* swaps the elements */

void swap(int * x, int * y)
{
    	int temp;
    	temp = *x;
    	*x = *y;
    	*y = temp; 
}
/* sorts the array using oddeven algorithm */

void oddeven_sort(int * x,int MAX)
{
    	int sort = 0, i;
    	while (!sort)
    	{
        	sort = 1;
        	#pragma omp parallel for
        	for (i = 1;i < MAX;i += 2)
	        {
			if (x[i] > x[i+1])
			{
		                swap(&x[i], &x[i+1]);
		                sort = 0;
		        }
        	}
          	#pragma omp parallel for
        	for (i = 0;i < MAX - 1;i += 2)
        	{
	            	if (x[i] > x[i + 1])
			{
		                swap(&x[i], &x[i + 1]);
				sort = 0;
	            	}
        	}
    	}
}
