import zope.component
import ZPublisher.pubevents
import zope.event
import types
import AccessControl
import logging
import Products.zopemods as zopemods

logger = logging.getLogger('Products.zopemods.protectedPythonScripts')
protected_meta_types = [
    'Script (Python)',
]
exposer_suffix = [
    '_ext',
]

def is_protected(obj):
    if not hasattr(obj, 'meta_type'):
        return False

    if obj.meta_type not in protected_meta_types:
        return False

    name_source = getattr(obj, 'getId', None)
    if not name_source:
        name_source = getattr(obj, 'title', None)

    if name_source is not None:
        if callable(name_source):
            name = name_source()

        for exposer in exposer_suffix:
            if name.endswith(exposer):
                return False
    else:
        logger.warning(f'{obj.request.URL0} has no name_source')
    
    return True


@zope.component.adapter(ZPublisher.pubevents.PubAfterTraversal)
def protectedURLHandler(event):
    # Managers may view anything they want.
    if event.request.AUTHENTICATED_USER.has_role('Manager'):
        return

    # Two possibilities: either we have an instancemethod, or a
    # product instance (Python Script or others)
    if isinstance(event.request.PUBLISHED, types.MethodType):
        # For methods we need the immediate parent
        obj = event.request.PARENTS[0]
    else:
        # For product instances we take the object itself.
        obj = event.request.PUBLISHED
    
    try:
        protection_enabled = zopemods.getContextProperty(
            context=obj,
            name='protectPythonScripts_',
            default=True,
        )
    except AttributeError:
        protection_enabled = False

    if is_protected(obj) and protection_enabled:
        raise AccessControl.Unauthorized()


zope.component.provideHandler(protectedURLHandler)
