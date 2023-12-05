#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *reversed;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	reversed = reverse_list(slow);
	while (reversed != NULL)
	{
		if ((*head)->n != reversed->n)
			return (0);
		*head = (*head)->next;
		reversed = reversed->next;
	}
	return (1);
}

/**
 * reverse_list - Reverses a linked list.
 * @node: The head of the list to be reversed.
 *
 * Return: The head of the reversed list.
 */
listint_t *reverse_list(listint_t *node)
{
	listint_t *prev = NULL;
	listint_t *current = node;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
