#include <stdio.h>
int main(int argc, char const *argv[])
{
    int age;
    float weight;
    char first[15], last[15]; /* 2 char arrays
    */
   printf("\nWhat is your first name?");
   scanf(" %s", first); /* No ampersand on
   char arrays*/
   printf("What is your last name?");
   scanf("%s", last);

   printf("How old are you?");
   scanf("%d", &age); /* Ampersand required*/
   printf("How much do you weigh?");
   scanf(" %f", &weight); /* Ampersand required*/

   printf("\nHere is the infomration you entered:\n");
   printf("Name: %s %s\n", first, last);
   printf("Weight: %3.0f\n", weight);
   printf("Age: %d", age);
   return 0; /* Always best to do this */
}


