#include"lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle int it
 * @list: pointer to listint_t
 * Return: 0 if there is no cycle, 1 if there is a cycle
 **/

int check_cycle(listint_t *list)
{
	listint_t *i = list;
	listint_t *j = list;

	while (i != NULL && j != NULL && j->next)
	{
		i = i->next;
		j = j->next->next;

		if (j == i)
			return (1);
	}
	return (0);
}
