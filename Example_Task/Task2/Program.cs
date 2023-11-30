Console.Clear();
int numberA = new Random().Next(0,10);
Console.WriteLine(numberA);
int max = numberA;
int min = numberA;
int numberB = new Random().Next(0,10);
Console.WriteLine(numberB);

if (numberB > max) max = numberB;

if (numberB < min) min = numberB;

Console.Write("max=");
Console.WriteLine(max);
Console.Write("min=");
Console.WriteLine(min);