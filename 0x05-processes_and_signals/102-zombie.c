#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_loop - creates an infinite loop
 * Return: always 0
 */
int infinite_loop(void)
{
while (1)
{
sleep(1);
}
return (0);
}
/**
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
int i;
pid_t zombies;
for (i = 0; i < 5; i++)
{
zombies = fork();
if (!zombies)
return (0);
printf("Zombie process created, PID: %d\n", zombies);
}
infinite_while();
return (0);
}
