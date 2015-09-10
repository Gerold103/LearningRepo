# -*- coding: utf-8 -*-


def bubble_sort(array, key=None, reverse=False):

	for i in range(len(array)):
		for j in range(len(array) - i -1):
			left = None
			right = None
			if key:
				left = key(array[j])
				right = key(array[j + 1])
			else:
				left = array[j]
				right = array[j + 1]
			if left > right:
				array[j], array[j + 1] = array[j + 1], array[j]
	if reverse == True:
		return sorted(array, reverse=True)
	else:
		return array


def reversed_bubble(array, key=None):

	for i in range(len(array)):
		for j in reversed(range(1 + i, len(array))):
			left = None
			right = None
			if key:
				right = key(array[j])
				left = key(array[j - 1])
			else:
				right = array[j]
				left = array[j - 1]
			if right > left:
				array[j], array[j - 1] = array[j - 1], array[j]
	return array





