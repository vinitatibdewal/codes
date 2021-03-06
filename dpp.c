#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
                                                //macro definition
#define EATINGTIME 1
                                    //function prototype for the thread function.
void * philosopher1();
void * philosopher2();
void * philosopher3();
void * philosopher4();
void * philosopher5();
                                    //global decalration of semaphore variables.
sem_t sem15,sem12,sem23,sem34,sem45;
                                    //global variable to control the execution of main.
int end=0;
int main()
{
//char a[2];
pthread_t t1,t2,t3,t4,t5;
pthread_attr_t at1;
pthread_attr_init(&at1);

sem_init(&sem15,0,1);	//0=non shared 1=initial value assigned
sem_init(&sem12,0,1);
sem_init(&sem23,0,1);
sem_init(&sem34,0,1);
sem_init(&sem45,0,1);

pthread_create(&t3,&at1,philosopher3,NULL);	
pthread_create(&t1,&at1,philosopher1,NULL);
pthread_create(&t4,&at1,philosopher4,NULL);
pthread_create(&t2,&at1,philosopher2,NULL);
pthread_create(&t5,&at1,philosopher5,NULL);
while(end!=5)
{
}
}
                        //definition of philosopher1.
void * philosopher1()
{
int i=0;
printf("\n\t\tPHILOSOPHER-1 THINKING.\n");
while(i<EATINGTIME)
{
sleep(1);
                        //waiting to acquire the forks.
sem_wait(&sem15);
sem_wait(&sem12);
printf("\n\t\t\t* PHILOSOPHER-1 EATING.*\n");
sleep(1);
                        //releasing the forks
sem_post(&sem15);
sem_post(&sem12);
printf("\n\t\tPHILOSOPHER-1 THINKING.\n");
i++;
}
end++;
}
                        //philosopher2.
void * philosopher2()
{
int i=0;
printf("\n\t\tPHILOSOPHER-2 THINKING.\n");
while(i<EATINGTIME)
{
sleep(1);
sem_wait(&sem12);
sem_wait(&sem23);
printf("\n\t\t\t* PHILOSOPHER-2 EATING.*\n");
sleep(1);
sem_post(&sem12);
sem_post(&sem23);
printf("\n\t\tPHILOSOPHER-2 THINKING.\n");
i++;
}
end++;
}
                                    //philosopher 3
void * philosopher3()
{
int i=0;
printf("\n\t\tPHILOSOPHER-3 THINKING.\n");
while(i<EATINGTIME)
{
sleep(1);
sem_wait(&sem23);
sem_wait(&sem34);
printf("\n\t\t\t* PHILOSOPHER-3 EATING.*\n");
sleep(1);
sem_post(&sem23);
sem_post(&sem34);
printf("\n\t\tPHILOSOPHER-3 THINKING.\n");
i++;
}
end++;
}
                                                //philosopher 4.
void * philosopher4()
{
int i=0;
printf("\n\t\tPHILOSOPHER-4 THINKING.\n");
while(i<EATINGTIME)
{
sleep(1);
sem_wait(&sem34);
sem_wait(&sem45);
printf("\n\t\t\t* PHILOSOPHER-4 EATING.*\n");
sleep(1);
sem_post(&sem34);
sem_post(&sem45);
printf("\n\t\tPHILOSOPHER-4 THINKING.\n");
i++;
}
end++;
}
                                                //philosopher 5.
void * philosopher5()
{
int i=0;
printf("\n\t\tPHILOSOPHER-5 THINKING.\n");
while(i<EATINGTIME)
{
sleep(1);
sem_wait(&sem45);
sem_wait(&sem15);
printf("\n\t\t\t* PHILOSOPHER-5 EATING.*\n");
sleep(1);
sem_post(&sem45);
sem_post(&sem15);
printf("\n\t\tPHILOSOPHER-5 THINKING.\n");
i++;
}
end++;
}
