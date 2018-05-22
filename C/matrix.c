#include <stdio.h>
#include <math.h>
#define F1 3
#define C1 3
#define F2 3
#define C2 3

//changing a number
void new_number(float *n); //al pasar el puntero se actualizara la informacion de la variable globalmente
float dot_product(float *v1, float *v2, int l1);

int  main(void){
    
    int i,j,k,l=0;
    
    //Definiendo matrices---------------------------------------
    
    int M1[F1][C1]={{1,0,0},{0,1,0},{0,0,1}};
    int M2[F2][C2]={{1,1,1},{1,1,1},{1,1,1}};
    
    printf("primera matriz \n");
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            printf("%d ", M1[i][j]);
        }
        printf("\n");
    }

    printf("segunda matriz \n");
    for(i=0;i<F1;i++){
        for(j=0;j<C1;j++){
            printf("%d ", M2[i][j]);
        }
        printf("\n");
    }
    
    float n=1.0;
    
    printf("before %f \n", n);
    
    new_number(&n);//se debe pasar la direccion de informacion de la variable para que esta sea modificada
    
    printf("after %f \n", n);
    
    
    //funciones de Arreglos--------------------
    
    int l1=3;
    float v1[l1],v2[l1];// se definen arreglos de cierto tamaño----------------------------------------
    
    for(i=0;i<l1;i++){
        v1[i]=i;
        v2[i]=i*i;
        printf("%f, %f \n",v1[i],v2[i]);
    }
    float v1xv2=dot_product(v1,v2,l1);//pasar arreglos a funciones
    printf("dot product = %f \n", v1xv2);
   
    

return 0;
}

//---------------FUNCIONES---------------------------

void new_number(float *n){
    
    *n=*n+1.0;
}


float dot_product(float *v1, float *v2, int l1){
    
    int i,j=0;
    float suma=0;
    
    for(i=0;i<l1;i++){
        printf(" v1[%d]=%f, v2[%d]=%f \n",i,v1[i],i,v2[i]);
        suma+=v1[i]*v2[i];
    }
    printf("suma=%f\n",suma);
    return suma;
}



















