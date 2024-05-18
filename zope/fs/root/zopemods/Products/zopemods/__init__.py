from Products.PythonScripts.Utility import allow_module


allow_module('json')
__import__('Products.zopemods.requestWrapper')
__import__('Products.zopemods.protectedPythonScripts')
