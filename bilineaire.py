# -*- coding: utf-8 -*-
'''
Created on 2019/10/02
@author: Jean-Pierre
fonction interpolation bilineaire   '''

def interpol( x, y, x1, y1, x2, y2, f_x1_y1, f_x1_y2, f_x2_y2, f_x2_y1):
    '''x,y coordonnees du point recherche'''
    '''x1,y1,x2,y2 coordonnees des coins de l'interpolation'''
    '''f_x1_y1....   valeurs de la fonction aux quatres coins'''

    dx = x - x1
    dy = y - y1
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta_fx = f_x2_y1 - f_x1_y1
    delta_fy = f_x1_y2 - f_x1_y1
    delta_fxy = f_x1_y1 + f_x2_y2 - f_x2_y1 - f_x1_y2

    interpolation = (delta_fx * dx / delta_x) + (delta_fy * dy / delta_y) + (
            delta_fxy * dx * dy / delta_x / delta_y) + f_x1_y1

    return interpolation


if __name__ == "__main__":
    x1, y1 = 2, 2
    x2, y2 = 4, 4

    f_x1_y1 = 100.
    f_x1_y2 = 200.
    f_x2_y2 = 300.
    f_x2_y1 = 200.

    x, y = 2.5, 2.5

    print ('Interpolation bilineaire sur les valeurs : ')
    print ('x1, y1 = ',x1,y1)
    print ('x2, y2 = ', x2,y2)
    print('f_x1_y1 ,f_x1_y2 , f_x2_y2 ,f_x2_y1 = ',f_x1_y1 ,f_x1_y2 , f_x2_y2 ,f_x2_y1)
    print('x1, y1 = ', x1, y1)


    a = interpol(x, y, x1, y1, x2, y2, f_x1_y1, f_x1_y2, f_x2_y2, f_x2_y1)
    print('\nvaleur de l\'interpolation de la  fonction :',a)

