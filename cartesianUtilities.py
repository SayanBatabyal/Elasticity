import sympy as sp

x,y = sp.symbols('x, y')

f = sp.Function('f')(x,y)

E, nu = sp.symbols('E, nu')

def cartesianLaplacian(f):
    return (sp.diff(f,x,2)+sp.diff(f,y,2)).simplify()

def cartesianbiharmonic(f):
    return cartesianLaplacian(cartesianLaplacian(f)).simplify()

def sigma_xx(f):
    return sp.diff(f,y,2).simplify()

def sigma_yy(f):
    return sp.diff(f,x,2).simplify()

def sigma_xy(f):
    return sp.diff(sp.diff(f,x),y).simplify()

def epsilon_xx(sigma_xx, sigma_yy):
    return (1/E)*(sigma_xx-nu*sigma_yy).simplify()

def epsilon_yy(sigma_yy, sigma_xx):
    return (1/E)*(sigma_yy-nu*sigma_xx).simplify()

def epsilon_xy(sigma_xy):
    return ((1+nu)/E)*sigma_xy.simplify()