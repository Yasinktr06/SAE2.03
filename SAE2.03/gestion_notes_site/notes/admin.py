from django.contrib import admin
from .models import Etudiant, UE, Ressource, Enseignant, Examen, Note

admin.site.register([Etudiant, UE, Ressource, Enseignant, Examen, Note])
