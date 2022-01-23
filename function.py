import re
temp = []
def regular_text(list_contact):
    for res_upd in list_contact:
        pattern2 = re.sub(
            r"(\+7|8)(\s*\((\d+)\)\s*(\d+)\-(\d+)\-(\d+)|(\d+)|\s*(\d+)\-*(\d+)\-(\d+))(\s*((\w+\.\s\d+)|\((\w+\.\s\d+)\))*)",
            r"+7\3\4\5\6\7\8\9\10 \13\14", (res_upd[5]))
        pattern3 = re.findall(r"[А-Я][а-я]\w+", (res_upd[1]))
        pattern4 = re.findall(r"[А-Я][а-я]\w+", (res_upd[0]))
        if len(pattern4) == 3:
            temp.append(
                {'lastname': pattern4[2], 'firstname': pattern4[1], 'surname': pattern4[0], 'organization': res_upd[3],
                 'position': res_upd[4], 'phone': pattern2, 'email': res_upd[6]})
        elif len(pattern3) == 2:
            temp.append(
                {'lastname': pattern3[1], 'firstname': pattern3[0], 'surname': pattern4[0], 'organization': res_upd[3],
                 'position': res_upd[4], 'phone': pattern2, 'email': res_upd[6]})
        elif len(pattern3) == 1:
            temp.append(
                {'lastname': res_upd[2], 'firstname': res_upd[1], 'surname': res_upd[0], 'organization': res_upd[3],
                 'position': res_upd[4], 'phone': pattern2, 'email': res_upd[6]})
        elif len(pattern4) == 2:
            temp.append(
                {'lastname': res_upd[2], 'firstname': pattern4[1], 'surname': pattern4[0], 'organization': res_upd[3],
                 'position': res_upd[4], 'phone': pattern2, 'email': res_upd[6]})
    return temp

def mergeDict(dict1, dict2):
    for k, v in dict2.items():
        if dict1[k] == '':
            dict1[k] = v
    return dict1


def union(dict):
    temp_end = []
    for temp_1 in dict:
        name = temp_1['firstname']
        surname = temp_1['surname']
        temp3 = []
        merge_dict = {}
        for temp_2 in temp:
            if name == temp_2['firstname'] and surname == temp_2['surname']:
                temp3.append(
                    {'lastname': temp_2['lastname'], 'firstname': temp_2['firstname'], 'surname': temp_2['surname'],
                     'organization': temp_2['organization'], 'position': temp_2['position'], 'phone': temp_2['phone'],
                     'email': temp_2['email']})
        if len(temp3) >= 2:
            count = len(temp3)
            for temp4 in range(count - 1):
                merge_dict = mergeDict(temp3[temp4], temp3[temp4 + 1])
            temp_end.append({'lastname': merge_dict['lastname'], 'firstname': merge_dict['firstname'],
                             'surname': merge_dict['surname'], 'organization': merge_dict['organization'],
                             'position': merge_dict['position'], 'phone': merge_dict['phone'],
                             'email': merge_dict['email']})
        else:
            temp_end.append(
                {'lastname': temp3[0]['lastname'], 'firstname': temp3[0]['firstname'], 'surname': temp3[0]['surname'],
                 'organization': temp3[0]['organization'], 'position': temp3[0]['position'], 'phone': temp3[0]['phone'],
                 'email': temp3[0]['email']})
    return temp_end


def remove_recurrence(remowe_dict):
    for temp5 in remowe_dict:
        remove_index = []
        count = 0
        name = temp5['firstname']
        surname = temp5['surname']
        lastname = temp5['lastname']
        for dict2 in range(len(remowe_dict)):
            if remowe_dict[dict2]['firstname'] == name and remowe_dict[dict2]['surname'] == surname and remowe_dict[dict2]['lastname'] == lastname:
                count = count + 1
                remove_index.append(dict2)
        temp = remove_index
        if count >= 2:
            for temp_var in range(len(remove_index)):
                delete_var = remove_index[temp_var]
                if temp_var != 0:
                    del remowe_dict[delete_var]
    return remowe_dict