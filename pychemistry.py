#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""PyChemistry - это программа, созданная для помощи людям, изучающие химию
Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
from pychemistry.PeriodicTable import spell, PeriodicTable


def parse_elements_from_word(word):
	spellings = '{}'.format(spell(word))
	print(spellings)


def main():
	print('Введите химическую формулу: ')
	chemistry_formule = input(' > ')

	chemistry_not_digits = ''

	parse_elements_from_word(chemistry_formule)
	pertable = PeriodicTable()

	a = pertable.calculate_relative_molecular_mass(chemistry_formule)
	print(a)


if __name__ == '__main__':
	main()
