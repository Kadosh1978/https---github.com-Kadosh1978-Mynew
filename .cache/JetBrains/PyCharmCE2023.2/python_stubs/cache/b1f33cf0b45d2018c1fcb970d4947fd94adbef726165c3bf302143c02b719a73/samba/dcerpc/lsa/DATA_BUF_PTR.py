# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python3/dist-packages/samba/dcerpc/lsa.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import misc as __misc
import talloc as __talloc


class DATA_BUF_PTR(__talloc.BaseObject):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PIDL-generated element of base type lsa_DATA_BUF"""



