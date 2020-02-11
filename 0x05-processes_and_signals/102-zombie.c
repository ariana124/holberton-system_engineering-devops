#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - created an infinite loop
 *
 * Return: void
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - creates 5 zombie processes
 *
 * Return: void
 */
int main(void)
{
	int pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}

	infinite_while();
	return (0);
}
