//По заданному номеру дня недели вывести его название
Console.Clear();
Console.WriteLine("Введите число от 1 до 7 ");
string numbes = Console.ReadLine(); //Компютер запоминает введенное число
int day = Convert.ToInt16(numbes);
//int day = number;

if (day == 1)
{
    Console.WriteLine("Понедельник");
}
if (day == 2)
{
    Console.WriteLine("Вторник");
}
if (day == 3)
{
    Console.WriteLine("Среда");
}
if (day == 4)
{
    Console.WriteLine("Четверг");
}
if (day == 5)
{
    Console.WriteLine("Пятница");
}
if (day == 6)
{
    Console.WriteLine("Суббота");
}
if (day == 7)
{
    Console.WriteLine("Воскресень");
}
