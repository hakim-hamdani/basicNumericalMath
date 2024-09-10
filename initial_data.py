

def intial_data():
    """
    Renvoie un dictionnaire avec les valeurs initiales des paramètres.
    """
    parametres = {
        'kf': 1.,
        'Afx': 1.,
        'Afy': 1.,
        'dxf': 1.,
        'dX': 1.,
        'dY': 1.,
        'Sc': 0.,
        'Sp': 0.,
        'Tbw': 100.,
        'Tbe': 100.,
        'Tbn': 200.,
        'Tbs': 80.,
        'Qbw': 0.,
        'Qbe': 0.,
        'Qbn': 0.,
        'Qbs': 0.,
        'BC_T_Imin': 'Dirichlet',
        'BC_T_Imax': 'Newmann',
        'BC_T_Jmin': 'Dirichlet',
        'BC_T_Jmin': 'Dirichlet'
    }
    return parametres