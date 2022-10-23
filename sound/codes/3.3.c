#include <stdio.h>
float yn(int* x,int  n){
   int y=0;
   if(n==0){y =*p1;}
   else if(n==1){
   y=*(x+1)+yn(x,0);
   }
   else if(n<6){
   y = *(x+n-1) + *(x+n-3) - yn(x,n-1)*0.5;
   }
   else {
   y = -yn(x,n-1)*0.5;
   }
   return y;
}

int main(){
FILE* fp;
const int Points;
int x[];
float y[Points];
int i;

x={1,2,3,4,2,1};
Points=20;

for(int i=0;i<number_Of_Points;i++){
y[i]=yn(x,i);
}

fp = fopen("y(n).dat","w");

for(i=0;i<number_Of_Points;i++){
fprintf(fp,"%f\n",y[i]);
}

fclose(fp);
return 0; 
}
