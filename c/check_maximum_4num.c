#include<stdio.h>
int main(){
  int a,b,c,d;
  scanf("%d%d%d%d", &a, &b, &c, &d);
  int max = (a>b)? a: b;
  max = (max>c)? max : c;
  max = (max>d)? max : d;
  int min = (d<c)? d:c;
  min = (min<c)? min : c;
  min = (min<b)? min : b;
  min = (min<a)? min : a;
  printf("Maximum is :%d\n", max);
  printf("Minimum is :%d", min);
}