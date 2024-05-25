from Products.PythonScripts.Utility import allow_module


allow_module('json')
__import__('Products.zopemods.requestWrapper')
__import__('Products.zopemods.protectedPythonScripts')


def getAbsoluteParent(obj):
    parent_id = obj.getPhysicalPath()[-2]

    if parent_id != '':
        return getattr(obj, parent_id)
    else:
        return obj.getPhysicalRoot()


def getContextProperty(context, name, default=None):
    prop_val = context.getProperty(name, None)

    if prop_val != None:
        return prop_val

    if getattr(context, 'isTopLevelPrincipiaApplicationObject'):
        return default
    
    if not hasattr(context, 'getParentNode'):
        return default


    abs_parent = getAbsoluteParent(context)
    return getContextProperty(abs_parent, name, default)