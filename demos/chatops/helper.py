#!/usr/bin/env python

import netaddr

def validate_network(net):
    pass

def get_ipmask(net):
    try:
        ip, mask = net.split("/")
    except ValueError:
        net = f"{net}/32"
    ip, mask = net.split("/")
    network = netaddr.IPNetwork(net)
    return dict(ip_address=ip, ip_mask=str(network.netmask))

def validate_input(user_input):
    #{u'protocol': u'tcp', u'source_network': u'10.3.3.3', u'destination_network': u'10.0.0.0/24', u'port': u'2222'}
    result = {
        'protocol': user_input['protocol'],
        'dst_port': user_input['port'],
        'action': user_input['action'],
        'src_network': get_ipmask(user_input['source_network']).get(
            'ip_address'
        ),
    }

    result['src_mask'] =  get_ipmask(user_input['source_network']).get('ip_mask')
    result['dst_network'] = get_ipmask(user_input['destination_network']).get('ip_address')
    result['dst_mask'] =  get_ipmask(user_input['destination_network']).get('ip_mask')
    return result
