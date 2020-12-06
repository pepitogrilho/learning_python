# -*- coding: utf-8 -*-


def both_tuple_dict(*args, **kwargs):
    print(args)
    print(kwargs)
    
both_tuple_dict(1,2,3, x=1, y=2)