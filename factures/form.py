from .models import *
from django.forms import inlineformset_factory

form_ligne = inlineformset_factory(Proposition, Ligne, fields='__all__')
