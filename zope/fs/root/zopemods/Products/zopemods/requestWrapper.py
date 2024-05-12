#
# Hook into event handlers to call request_init/request_end
#

import zope.component
import ZPublisher.pubevents


def get_context(event):
    title = getattr(event.request.PUBLISHED, 'title', None)
    if title is None:
        return None
    if callable(title):
        title = title()

    try:
        context = event.request.PARENTS[0]
        return context
    except Exception:
        return None


@zope.component.adapter(ZPublisher.pubevents.PubAfterTraversal)
def request_init(event):
    # Do not call request_init on manage pages
    url = event.request.getURL()
    url_ending = url.split('/')[-1]
    if url_ending.startswith('manage'):
        return

    context = get_context(event)
    if hasattr(context, 'request_init'):
        init_ret = context.request_init()

        if isinstance(init_ret, dict):
            for key in init_ret.keys():
                event.request.set(key, init_ret.get(key))


@zope.component.adapter(ZPublisher.pubevents.PubBeforeCommit)
def request_end(event):
    # Do not call request_end on manage pages
    url = event.request.getURL()
    url_ending = url.split('/')[-1]
    if url_ending.startswith('manage'):
        return

    context = get_context(event)
    if hasattr(context, 'request_end'):
        context.request_end()


zope.component.provideHandler(request_init)
zope.component.provideHandler(request_end)
print(':3')