def sum_pays(qs) -> dict:
    dict_sum = {
        'communal_pay': [],
        'electric_pay': [],
        'internet_pay': [],
        'antenna_pay':  [],
        'doorphone_pay': [],
        'doorphone_pay2': [],
    }
    for el in qs:
        dict_sum['communal_pay'].append(el.communal_pay)
        dict_sum['electric_pay'].append(el.electric_pay)
        dict_sum['internet_pay'].append(el.internet_pay)
        dict_sum['antenna_pay'].append(el.antenna_pay)
        dict_sum['doorphone_pay'].append(el.doorphone_pay)
        dict_sum['doorphone_pay2'].append(el.doorphone_pay2)


    for key in dict_sum:
        dict_sum[key] = sum(dict_sum[key])

    return dict_sum