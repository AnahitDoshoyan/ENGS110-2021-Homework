#include <iostream>

int fibonacci_sum(int n)
{
        int f1 = 0;
        int f2 = 1;
        int sum = 0;
        if (n >= 0) {
                int temp = 0;
                while (f2 <= n) {
                        sum = sum + f2;
                        temp = f1 + f2;
                        f1 = f2;
                        f2 = temp;
                }
 
                 printf("The sum is = %d\n", sum);
         }
         return sum;
 }
 

 void print_binary(int a)
 {
         int c = 0;
 
 
         printf ("%d in binary is:\n", a);
 
         for (int b = sizeof(int) * 8 - 1; b >= 0; b--) {
                 c = a % 2;
                 a = a >> 1;
                 if (c & 1) {
                         printf ("1");
                 } else {
                         printf ("0");
                }
        }
 
         printf("\n");
}
  
int main()
{
        int n = 0;
        printf("PLease input your age: ");
        scanf("%d", &n);
	int z = fibonacci_sum(n);
        print_binary(z);
}
