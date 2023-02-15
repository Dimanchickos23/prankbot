import requests

# Полная и актуальная документация по API: https://calltools.ru/guide_api


CALLTOOLS_PUBLIC_KEY = '34bef68cacd64183d3cf70dbb14a43df '
CALLTOOLS_BASE_URL = 'https://calltools.ru'
CALLTOOLS_TIMEOUT = 30


class CallToolsException(Exception):
    pass


def check_a_status(campaign_id, phonenumber, call_id=None):
    if phonenumber:
        url = '/lk/cabapi_external/api/v1/phones/calls_by_phone/'
    elif call_id:
        url = '/lk/cabapi_external/api/v1/phones/call_by_id/'
    else:
        raise ValueError('check_status required call_id or phonenumber')

    resp = requests.get(CALLTOOLS_BASE_URL + url, {
        'public_key': CALLTOOLS_PUBLIC_KEY,
        'phone': phonenumber,
        'call_id': call_id,
        'campaign_id': campaign_id,
    }, timeout=CALLTOOLS_TIMEOUT)

    ret = resp.json()
    print(ret[0])
    prank_info = ret[0]
    print(prank_info[''])
    if ret['status'] == 'error':
        raise CallToolsException(ret['data'])
    return


# def check_a_status(campaign_id,call_id):
#     if call_id:
#         url = '/lk/cabapi_external/api/v1/phones/call_by_id/'
#     else:
#         raise ValueError('check_status required call_id or phonenumber')
#     resp = requests.get(CALLTOOLS_BASE_URL + url, {
#         'public_key': CALLTOOLS_PUBLIC_KEY,
#         'call_id': call_id,
#         'campaign_id': campaign_id,
#     }, timeout=CALLTOOLS_TIMEOUT)
#     ret = resp.json()
#     print(ret)
#     if ret['status'] == 'error':
#         raise CallToolsException(ret['data'])
#     return


# check_a_status(740068322,2212071766317774)


def call_ncreate_call(campaign_id, numb):
    try:
        resp = requests.get(CALLTOOLS_BASE_URL + '/lk/cabapi_external/api/v1/phones/call/', {
            'public_key': CALLTOOLS_PUBLIC_KEY,
            'phone': +numb,
            'campaign_id': campaign_id,
        }, timeout=CALLTOOLS_TIMEOUT)
        ret = resp.json()
        if ret['status'] == 'error':
            return False
        else:
            pass
    except Exception as e:
        print(e)
        return False


def new_check_call(campaign_id, numb):
    print('Ok..')
    url = '/lk/cabapi_external/api/v1/phones/calls_by_phone/'
    resp = requests.get(CALLTOOLS_BASE_URL + url, {
        'public_key': CALLTOOLS_PUBLIC_KEY,
        'phone': +numb,
        'campaign_id': campaign_id
    }, timeout=CALLTOOLS_TIMEOUT)
    ret = resp.json()
    resolt_prank_info = ret[0]
    return resolt_prank_info
    # for r in ret:
    #     print(r)
    # if r['status'] == 'compl_finished':
    #     return r['recorded_audio']
    # if r['status'] == 'in_process':
    #     return 1
    # if r['dial_status_display'] == 'Ответил автоответчик':
    #     return False
    # else:
    #     return False
