#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - a C function that prints some basic info about,
 * Python lists.
 *@p: a pointer to a Python object
 * Return: basic info about python lists.
 **/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	i = 0
		while (i < size) 
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
			i++;
		}
}
