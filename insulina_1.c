//sistem needs to ask for correction boulos (dg/ml per carb) and the quantity os carbs ingested

/*ex: 
foodBoulos = 15 #input
carbs = 30g #input
insulinQuantity = carbs/boulos #process/output
insulinQuantityMax = ? #input
maxCarbQuantity = boulos * insulin quantity max #process
remaningInsulinPerDay = insulin quntity max - insulin quntity
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int foodBoulos, carbs, insulinQuantity, insulinQuantityMax, maxCarbQuantity, remaningInsulinPerDay;
    char name[20];
    printf("Input your name: ");
    gets(name);
    printf("Input bolus quantity per carbohydrate: ");
    scanf("%d", &foodBoulos);
    printf("Input carbohydrate quantity ingested: ");
    scanf("%d", &carbs);
    insulinQuantity = carbs/foodBoulos;
    printf("Input maximum insulin quantity prescribed: ");
    scanf("%d", &insulinQuantityMax);
    maxCarbQuantity = foodBoulos * insulinQuantityMax;
    remaningInsulinPerDay = insulinQuantityMax - insulinQuantity;
    printf("The insulin quantity to digest %dg is %d\n", carbs, insulinQuantity);
    printf("Your maximum carbohydrate quantity is %dg\n", maxCarbQuantity);
    printf("Your remaining insulin of the day is %d\n", remaningInsulinPerDay);
    return 1;
}
