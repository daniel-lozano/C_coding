#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define F1 3
#define C1 3
#define F2 3
#define C2 3

//changing a number

void print_matrix( int **M1);
void multiply_matrix( int **M1, int **M2, int **M3 );
void x2( int *M1);
void x2_pointer( int **M1);

int  main(void){
    
    int i,j,k,l=0;
    
    //Definiendo matrices con punteros---------------------------------------
    
    int *M1;
    M1=malloc(sizeof(int)*F1*C1);
    
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            if(i==j){
                M1[i*C1+j]=1;
            }
            else{
                M1[i*C1+j]=0;
            }
            printf("%d ", M1[i*C1+j]);
        }
        printf("\n");
    }
    
    x2( M1);
    
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            printf("%d ", M1[i*C1+j]);
        }
        printf("\n");
    }
   //Definiendo matrices con punteros a punteros--------------------------------
    
    
    printf("matriz con punteros\n");
    
    int **m1 = (int **)malloc(F1 * sizeof(int *));
    int **m2 = (int **)malloc(F2 * sizeof(int *));
    int **m1x2 = (int **)malloc(F1 * sizeof(int *));
    for (i=0; i<F1; i++){m1[i] = (int *)malloc(C1 * sizeof(int));}
    for (i=0; i<F2; i++){m2[i] = (int *)malloc(C2 * sizeof(int));}
    for (i=0; i<F1; i++){m1x2[i] = (int *)malloc(C2 * sizeof(int));}
    
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            if(i==j){m1[i][j]=1;}
            else{m1[i][j]=0;}
        }}
    printf("m1=\n");
    print_matrix(m1);
    
    for(i=0;i<F2;i++){
        for(j=0;j<C2;j++){
            if(i<=j){m2[i][j]=1;}
            else{m2[i][j]=0;}
        }}
    printf("m2=\n");
    print_matrix(m2);
    
    printf("before m3=\n");
    print_matrix(m1x2);
    multiply_matrix(m1,m2,m1x2);
    printf("after m3=\n");
    print_matrix(m1x2);
    
  
    
  
   
    
    return 0;
}

//---------------FUNCIONES---------------------------

void x2( int *M1){
    int i,j=0;
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            M1[i*C1+j]*=2;
        }
    }
}

void x2_pointer( int **M1){
    int i,j=0;
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            M1[i][j]*=2;
        }
    }
}


void print_matrix( int **M1){
    int i,j=0;
    printf("Printing \n");
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            printf("%d ",M1[i][j]);
        }
        printf("\n");
    }
    
}

void multiply_matrix( int **M1, int **M2, int **M3 ){
    
    int i,j,k=0;
    int suma=0;
    
    for(i=0;i<F1;i++){
        for(j=0;j<C2;j++){
            for(k=0;k<C1;k++){
                suma+=M1[i][k]*M2[k][j];
            }
            M3[i][j]=suma;
            suma=0;
        }
    }
    
}

















