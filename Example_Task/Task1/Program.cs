//По двум заданным числам проверять является ли первое квадратом второго
//x=y^2
Console.Write("Введите x: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите y: ");
int y = Convert.ToInt32(Console.ReadLine());
if (x==y*y)
{
    Console.WriteLine("yes");
}
else
{
    Console.WriteLine("no");
}