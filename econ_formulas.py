# a bit of code to automate some homework for econ
# because why do something manually if you can take three times as long to automate it
# at least I learned what try and except do

def econ_calc():
    var = input("What variable would you like to compute?\n")
    var_options = ['Tau', 'Rt', 'Rt hat', 'Delta', 'Yt', 'Kt', 'Alpha', 'Capital Output Ratio', 'Labor Output Ratio'] 

    # check special cases
    if var == 'help':
        print(f'Variables that you can compute: {var_options}.')
        var = input()
    if var not in var_options:
        print('ERROR: Invalid Input')
        return None
    
    # calculate
    if var == 'Tau':
        ans = tau_calc()
        if ans != None:
            return f'Tau = {ans}'
        else:
            return None

    if var == 'Rt':
        ans = rt_calc()
        if ans != None:
            return f'Rt = {ans}'
        else:
            return None  

    if var == 'Rt hat':
        ans = rt_hat_calc()
        if ans != None:
            return f'Rt hat = {ans}'
        else:
            return None 
        
    if var == 'Delta':
        ans = delta_calc()
        if ans != None:
            return f'Delta = {ans}'
        else:
            return None
        
    if var == 'Yt':
        ans = yt_calc()
        if ans != None:
            return f'Yt = {ans}'
        else:
            return None
        
    if var == 'Kt':
        ans = kt_calc()
        if ans != None:
            return f'Kt = {ans}'
        else:
            return None
        
    if var == 'Lt':
        ans = lt_calc()
        if ans != None:
            return f'Lt = {ans}'
        else:
            return None
        
    if var == 'Zt':
        ans = zt_calc()
        if ans != None:
            return f'Zt = {ans}'
        else:
            return None

    if var == 'Alpha':
        ans = alpha_calc()
        if ans != None:
            return f'Alpha = {ans}'
        else:
            return None
    
    if var == 'Capital Output Ratio':
        ans = tau_calc()
        if ans != None:
            return f'Capital Output Ratio = {ans}'
        else:
            return None
        
    if var == 'Labor Output Ratio':
        ans = tau_calc()
        if ans != None:
            return f'Labor Output Ratio = {ans}'
        else:
            return None

    ['Tau', 'Rt', 'Rt hat', 'Delta', 'Yt', 'Kt', 'Lt', 'Zt', 'Alpha', 'Capital Output Ratio', 'Labor Output Ratio']
    
def tau_calc():
    # tau = 1 - (rt hat)/(rt-delta)
    try:
        rt_hat = float(input("What is rt hat?\n"))
        rt = float(input("Whst is rt?\n"))
        delta = float(input("What is delta?\n"))
        return 1 - rt_hat/(rt-delta)
    except:
        print('ERROR: Invalid Input')
        return None
    
def rt_calc():
    # rt = alpha*yt/kt or rt = (rt hat)/(1-tau) + delta
    choice = input("Which formula?: (1) rt = alpha*Yt/Kt or (2) rt = (rt hat)/(1-tau) + delta\n")

    if choice != 1 or choice != 2:
        print("ERRO: Invalid Input")
        return None
    elif choice == 1:
        try:
            alpha = float("What is alpha\n")
            yt = float("What is Yt?\n")
            kt = float("What is Kt?\n")
            return alpha * yt / kt
        except:
            print('ERROR: Invalid Input')
            return None
    else:
        try:
            rt_hat = float("What is rt hat?\n")
            tau = float("What is tau?\n")
            delta = float("What is delta?\n")
            return rt_hat/(1-tau) + delta
        except:
            print('ERROR: Invalid Input')
            return None

def rt_hat_calc():
    # rt hat = (1-Tau)(rt-delta)
    try:
        tau = float("What is tau?\n")
        rt = float("What is rt?\n")
        delta = float("Whst is delta?\n")
        return (1-tau)*(rt-delta)
    except:
        print('ERROR: Invalid Input')
        return None

def delta_calc():
    # delta = rt - (rt hat)/(1-tau)
    try:
        rt = float(input("What is rt?\n"))
        rt_hat = float(input("What is rt hat?\n"))
        tau = float(input("What is tau?\n"))
        return rt - rt_hat/(1-tau)
    except:
        print('ERROR: Invalid Input')
        return None

def yt_calc():
    # yt = zt * kt**alpha * lt**(1-alpha)
    try:
        zt = float(input("What is Zt?\n"))
        kt = float(input("What is Kt?\n"))
        lt = float(input("What is Lt?\n"))
        alpha = float(input("What is alpha?\n"))
        return zt * kt**alpha * lt**(1-alpha)
    except:
        print('ERROR: Invalid Input')
        return None

def kt_calc():
    # kt = (1-delta)*k(t-1)+It or kt = (Yt/(Zt * Lt**(1-alpha)))**(1/alpha)
    choice = input("Which formula?: (1) Kt = (1-delta)*K(t-1)+It or (2) Kt = (Yt/(Zt * Lt**(1-alpha)))**(1/alpha)\n")

    if choice != 1 or choice != 2:
        print("ERRO: Invalid Input")
        return None
    elif choice == 1:
        try:
            delta = float("What is delta\n")
            kt_0 = float("What is K(t-1)?\n")
            it = float("What is It?\n")
            return(1-delta)*kt_0 + it
        except:
            print('ERROR: Invalid Input')
            return None
    else:
        try:
            zt = float(input("What is Zt?\n"))
            lt = float(input("What is Lt?\n"))
            yt = float(input("What is Yt?\n"))
            alpha = float(input("What is alpha?\n"))
            return (yt/(zt * lt**(1-alpha))) ** (1/alpha)
        except:
            print('ERROR: Invalid Input')
            return None

def lt_calc():
    # Lt = (Yt/(Zt * Kt**alpha)) ** (1/(1-alpha))
    try:
        zt = float(input("What is Zt?\n"))
        kt = float(input("What is Kt?\n"))
        yt = float(input("What is Yt?\n"))
        alpha = float(input("What is alpha?\n"))
        return (yt/(zt * kt**alpha)) ** (1/(1-alpha))
    except:
        print('ERROR: Invalid Input')
        return None

def zt_calc():
    # Zt = Yt/(Kt**alpha * Lt**(1-alpha))
    try:
        yt = float(input("What is Yt?\n"))
        kt = float(input("What is Kt?\n"))
        lt = float(input("What is Lt?\n"))
        alpha = float(input("What is alpha?\n"))
        return yt/(kt**alpha * lt**alpha)
    except:
        print('ERROR: Invalid Input')
        return None

def alpha_calc():
    # alpha = rt * Kt / Yt
    try:
        rt = float(input("What is rt hat?\n"))
        kt = float(input("What is Kt?\n"))
        yt = float(input("What is Yt?\n"))
        return rt * kt / yt
    except:
        print('ERROR: Invalid Input')
        return None

def capital_output_ratio_calc():
    # ratio = Kt/Yt
    try:
        kt = float(input("What is Kt?\n"))
        yt = float(input("What is Yt?\n"))
        return kt / yt
    except:
        print('ERROR: Invalid Input')
        return None

def labor_output_ratio_calc():
    # ratio = Lt/Yt
    try:
        lt = float(input("What is Lt?\n"))
        yt = float(input("What is Yt?\n"))
        return lt / yt
    except:
        print('ERROR: Invalid Input')
        return None