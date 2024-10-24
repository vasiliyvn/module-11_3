import inspect


def introspection_info(obj):
    types = type(obj)
    attributes = dir(obj)
    methods_ = [method for method in attributes if callable(getattr(obj, method))]
    modules_ = obj.__class__.__module__
    doc_ = obj.__doc__
    denominator_ = obj.denominator
    info = {'type': types, 'attributes': attributes, 'methods': methods_, 'module': modules_, 'doc_': doc_,
            'denominator_': denominator_}
    return info


number_info = introspection_info(42)
print(number_info)
