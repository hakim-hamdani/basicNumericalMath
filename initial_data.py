

def intial_data():
    """
    Renvoie un dictionnaire avec les valeurs initiales des paramètres.
    """
    parametres = {
        'kf': 1.,
        'dxf': 1.,
        'dX': 1.,
        'dY': 1.,
        'dZ': 1.,
        'Sc': 0.,
        'Sp': 0.,
        'T_top'   : 400.,
        'T_bottom': 300.,
        'T_left'  : 100.,
        'T_right' : 200.,
        'Q_top'   : 0.,   # top-north
        'Q_bottom': 0.,   # bottom-south
        'Q_left'  : 0.,   # left-west
        'Q_right' : 0.,   # right-esast
        'BC_T_top'   : 'Dirichlet',
        'BC_T_bottom': 'Dirichlet',
        'BC_T_left'  : 'Dirichlet',
        'BC_T_right' : 'Dirichlet'
    }
    return parametres