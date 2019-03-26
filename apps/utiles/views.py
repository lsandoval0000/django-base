from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import *


class ProtectedView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def to_dict_from_list(objs, exclude=[]):
    tree = []
    for obj in objs:
        tree.append(to_dict_from_object(obj,exclude))
    return tree


def to_dict_from_object(obj, exclude=[]):
    tree = {}
    for field in obj._meta.fields + obj._meta.many_to_many:
        if field.name in exclude or \
           '%s.%s' % (type(obj).__name__, field.name) in exclude:
            continue
        try :
            value = getattr(obj, field.name)
        except obj.DoesNotExist as e:
            value = None
        except ObjectDoesNotExist as e:
            value = None
            continue
        if type(field) in [ForeignKey, OneToOneField]:
            tree[field.name] = to_dict_from_object(value, exclude=exclude)
        elif isinstance(field, ManyToManyField):
            vs = []
            for v in value.all():
                vs.append(to_dict_from_object(v, exclude=exclude))
            tree[field.name] = vs
        else:
            tree[field.name] = obj.serializable_value(field.name)
    return tree