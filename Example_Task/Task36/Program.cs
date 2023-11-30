//Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел
 Console.Write($"Укажите длинну массива ");
int l = Convert.ToInt32(Console.ReadLine());
int[] A = new int[l];  ///new Random().Next(100,999);
int Chetnoye = 0;
int not_even_ones = 0;
for (int i=0; i<l; i++)
{
    A[i] = new Random().Next(100, 1000);
    Console.Write($"[{A[i]}]");
    if (A[i] %2 == 0)
    {
        Chetnoye++;
    }
    else
    {
        not_even_ones ++;
    }
}
Console.WriteLine("");
Console.WriteLine($"Количество чётных чисел {Chetnoye}");
Console.WriteLine($"Количество нечётных чисел {not_even_ones}");