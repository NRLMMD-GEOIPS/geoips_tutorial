# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

def unpack_list_interface_by_type(by_type_dict):
    '''
    Function that unpacks the output from interface.list_<interface>_by_type dictionary to a list
    args:
        by_type_dict (dict): Output from geoips.dev.<interface>.list_<interface>_by_type()
    returns:
        (list): all func names available under a given interface
    '''
    return [x for xs in by_type_dict.values() for x in xs]


def func_name_check(func_name, interface_by_type_dict, interface):
    interfaces = {
                'reader': 'readers',
                'product': 'products',
                'alg': 'algorithms',
                'interp': 'interpolators',
                'filename': 'file names',
                'output': 'outputters',
                'output_config': 'output configs',
                'procflow': 'procflows',
                'cmap': 'color maps',
                'boundaries': 'boundaries',
                'gridlines': 'grid lines',
                'title': 'titles',
            }
    interface_names = interfaces[interface]
    all_funcs = unpack_list_interface_by_type(interface_by_type_dict)
    if func_name not in all_funcs:
        print(f'The interpolation function name you provided ({func_name}) is not availble in this GeoIPS install.')
        print(f'No worries, this will still be a good chance to see how the {interface} interface handles this bad function name')
        print(f'And for reference, here are the {interface_names} you can choose from:\n{all_funcs}')

def print_signatures(interface_by_type_dict, get_func, by_type=False):
    import inspect
    all_types = list(interface_by_type_dict.keys())
    type_sigs = {}
    for interface_type in sorted(all_types):
        interface_names = interface_by_type_dict[interface_type]
        for func_name in sorted(interface_names):
            interface_func = get_func(func_name)
            signature = inspect.signature(interface_func)
            if by_type:
                type_sigs[interface_type] = signature
            else:
                print(f'Type: {interface_type}, Name: {func_name},\n- Signature: {signature}\n')
    if by_type:
        for interface_type, signature in type_sigs.items():
            print(f'Type {interface_type} signature: {signature}\n')

def print_dict_structure(interface_by_type_dict, get_func):
    import inspect
    all_types = list(interface_by_type_dict.keys())
    for interface_type in sorted(all_types):
        interface_names = interface_by_type_dict[interface_type]
        for func_name in sorted(interface_names):
            interface_dict = get_func(func_name)
            keys = ', '.join(sorted(list(interface_dict.keys())))
            print(f'Type: {interface_type}, Name: {func_name},\n- Keys: {keys}\n')