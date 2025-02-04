EPSILON = 1e-5

DICT_ALIASES_CORE = {
    'node': 'NODE',
    'displacement': 'DISPLACEMENT',
    'disp': 'DISPLACEMENT',
    'nodal_stress': 'NodalSTRESS',
    'nodal_strain': 'NodalSTRAIN',
    'nodal_mises': 'NodalMISES',
    't_init': 'INITIAL_TEMPERATURE',
    't_cnt': 'CNT_TEMPERATURE',
    'reac': 'REACTION_FORCE',
    'elemental_stress': 'ElementalSTRESS',
    'elemental_strain': 'ElementalSTRAIN',
    'elemental_mises': 'ElementalMISES',
    'modulus': 'Young_modulus',
    'poisson_ratio': 'Poisson_ratio',
    'density': 'density',
    'lte': 'linear_thermal_expansion_coefficient',
    'lte_full': 'linear_thermal_expansion_coefficient_full',
    'specific_heat': 'specific_heat',
    'thermal_conductivity': 'thermal_conductivity',
    'orient': 'ORIENTATION',
    'boundary': 'boundary',
    'cload': 'cload',
    'fixtemp': 'fixtemp',
    'istrain1': 'GaussSTRAIN1',
    'istrain2': 'GaussSTRAIN2',
    'istrain3': 'GaussSTRAIN3',
    'istrain4': 'GaussSTRAIN4',
    'istrain5': 'GaussSTRAIN5',
    'istrain6': 'GaussSTRAIN6',
    'istrain7': 'GaussSTRAIN7',
    'istrain8': 'GaussSTRAIN8',
    'vf': 'VF',
    'pressure_start_shrinkage': 'pressure_start_shrinkage',
    'specific_volume_start_shrinkage': 'specific_volume_start_shrinkage',
    'average_temperature_start_shrinkage':
    'average_temperature_start_shrinkage',
    'time_start_shrinkage': 'time_start_shrinkage',
    'shrinkage': 'shrinkage',
    'gradient_temperature_mold': 'gradient_temperature_mold',
    'shrinkage_mold': 'shrinkage_mold',
    'pressure': 'pressure',
    'specific_volume': 'specific_volume',
    'average_temperature': 'average_temperature',
    'max_temperature': 'max_temperature',
    'thickness_flow_layer': 'thickness_flow_layer',
    'viscosity': 'viscosity',
    'shear_velocity': 'shear_velocity',
    'shear_stress': 'shear_stress',
    'flow_velocity': 'flow_velocity',
    'fiber_orientation_tensor': 'fiber_orientation_tensor',
    'fiber_orientation_vector': 'fiber_orientation_vector',
    'fiber_velocity': 'fiber_velocity',
    'skin_fiber_orientation_vector': 'skin_fiber_orientation_vector',
    'inflow_gate': 'inflow_gate',
    'flow_length': 'flow_length',
    'flow_length_by_thickness': 'flow_length_by_thickness',
    'temperature_difference': 'temperature_difference',
    'flow_front_time': 'flow_front_time',
    'normal': 'normal',
    'area': 'area',
}
DICT_ALIASES = dict(DICT_ALIASES_CORE)
DICT_ALIASES.update({
    v: v for v in DICT_ALIASES_CORE.values()})
DICT_INVERSE_ALIASES = {v: k for k, v in DICT_ALIASES_CORE.items()}
DICT_INVERSE_ALIASES.update({
    v: v for v in DICT_INVERSE_ALIASES.values()})
LIST_NODAL = [
    'node',
    'displacement',
    'disp',
    'nodal_mises',
    'nodal_stress',
    'nodal_strain',
    'reac',
    't_cnt',
    't_init',
    'pressure_start_shrinkage',
    'specific_volume_start_shrinkage',
    'average_temperature_start_shrinkage',
    'time_start_shrinkage',
    'shrinkage',
    'gradient_temperature_mold',
    'shrinkage_mold',
    'pressure',
    'specific_volume',
    'average_temperature',
    'max_temperature',
    'thickness_flow_layer',
    'temperature_difference',
    'flow_front_time',
]
LIST_ELEMENTAL = [
    'density',
    'elemental_mises',
    'elemental_strain',
    'elemental_stress',
    'istrain1',
    'istrain2',
    'istrain3',
    'istrain4',
    'istrain5',
    'istrain6',
    'istrain7',
    'istrain8',
    'lte',
    'lte_full',
    'modulus',
    'orient',
    'poisson_ratio',
    'vf',
    'viscosity',
    'shear_velocity',
    'shear_stress',
    'flow_velocity',
    'fiber_orientation_tensor',
    'fiber_orientation_vector',
    'fiber_velocity',
    'skin_fiber_orientation_vector',
]
LIST_CONSTRAINTS = [
    'boundary',
    'cload',
    'fixtemp',
]
LIST_MATERIALS = [
    'modulus',
    'poisson_ratio',
    'density',
    'lte',
    'lte_full',
    'specific_heat',
    'thermal_conductivity',
    'linear_thermal_expansion_coefficient',
    'linear_thermal_expansion_coefficient_full',
]

LINE_ELEMENT_NAMES = [
    'line',
    'line2',
]
SHELL_ELEMENT_NAMES = [
    'tri',
    'tri2',
    'quad',
    'quad2',
]
SOLID_ELEMENT_NAMES = [
    'line',
    'line2',
    'tet',
    'tet2',
    'pyr',
    'pyr2',
    'prism',
    'prism2',
    'hex',
    'hex2',
]

DICT_FEMIO_ELEMENT_TO_MESHIO_ELEMENT = {
    'pt': 'vertex',
    'line': 'line',
    'line2': 'line3',
    'tri': 'triangle',
    'tri2': 'triangle6',
    'quad': 'quad',
    'quad2': 'quad8',
    'tet': 'tetra',
    'tet2': 'tetra10',
    'pyr': 'pyramid',
    'pyr2': 'pyramid13',
    'prism': 'wedge',
    'prism2': 'wedge15',
    'hex': 'hexahedron',
    'hex2': 'hexahedron27',
    'hexprism': 'hexa_prism',
}
DICT_MESHIO_ELEMENT_TO_FEMIO_ELEMENT = {
    v: k for k, v in DICT_FEMIO_ELEMENT_TO_MESHIO_ELEMENT.items()}

DICT_EXT = {
    'fistr': '',
    'obj': 'obj',
    'stl': 'stl',
    'ucd': 'inp',
    'vtk': 'vtk',
}

DICT_VTK_ID_TO_ELEMENT_TYPE = {
    10: 'tet',
    12: 'hex',
    13: 'prism',
    14: 'pyr',
    42: 'polyhedron',
}

DICT_ELEMENT_TYPE_TO_VTK_ID = {
    v: k for k, v
    in DICT_VTK_ID_TO_ELEMENT_TYPE.items()}
