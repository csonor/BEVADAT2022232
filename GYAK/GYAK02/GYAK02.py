# %%
import numpy as np


def create_1d_array_zeros(size: int = 1) -> np.array:
    return np.zeros(size)


# %%


# %%
# FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
# Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
# Paraméterei: mérete (tuple-ként), default mérete pedig legyen egy (2,2)
# Be: (2,2)
# Ki: [[0,0],[0,0]]
# create_array()

# %%
def create_array(shape: tuple = (2, 2)) -> np.array:
    return np.zeros(shape, dtype=int).tolist()


# %%
# Készíts egy függvényt ami a paraméterként kapott array-t főátlóját feltölti egyesekkel
# Be: [[1,2],[3,4]]
# Ki: [[1,2],[3,1]]
# set_one()

# %%
def set_one(arr: np.array) -> np.array:
    np.fill_diagonal(arr, 1)
    return arr


# %%
# Készíts egy függvényt ami transzponálja a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()

# %%
def do_transpose(matrix: np.array) -> np.array:
    return np.transpose(matrix).tolist()


# %%
# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, ha nincs megadva ez a paraméter, akkor legyen az alapértelmezett a kettő
# Be: [0.1223, 0.1675], 2
# Ki: [0.12, 0.17]
# round_array()

# %%
def round_array(arr: np.array, n: int):
    return np.round(arr, n)


# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 0 - False-ra, az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()

# %%
def bool_array(arr: np.array) -> np.array:
    return np.array(arr, dtype=bool)


# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()

# %%
def invert_bool_array(arr: np.array) -> np.array:
    return np.where(arr, False, True)


# %%
# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()


# %%
def flatten(input_arr: np.array) -> np.array:
    return np.array(input_arr).flatten().tolist()