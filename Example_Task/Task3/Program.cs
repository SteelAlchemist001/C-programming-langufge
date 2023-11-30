//По заданному номеру дня недели вывести его название
Console.Clear();
string[] Weeks = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
Console.Write("Enter number: ");
Console.Write(Weeks[Convert.ToInt32(Console.ReadLine())-1]);