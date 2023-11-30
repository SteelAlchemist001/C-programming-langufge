int[] numbers ={1,7,9};
int size =3;
int index =0;
int max = numbers[0];
while (index<size) {
       if (numbers[index]>max){
           max =numbers[index];
       }
       index =index+1;
}
Console.WriteLine(max);
