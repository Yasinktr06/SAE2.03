from django.urls import path
from .views import (
    EtudiantList, EtudiantCreate, EtudiantUpdate, EtudiantDelete,
    UEList, UECreate, UEUpdate, UEDelete,
    RessourceList, RessourceCreate, RessourceUpdate, RessourceDelete,
    EnseignantList, EnseignantCreate, EnseignantUpdate, EnseignantDelete,
    ExamenList, ExamenCreate, ExamenUpdate, ExamenDelete,
    NoteList, NoteCreate, NoteUpdate, NoteDelete,
)

urlpatterns = [
    # Étudiants
    path('', EtudiantList.as_view(), name='etudiant_list'),
    path('etudiants/new/', EtudiantCreate.as_view(), name='etudiant_new'),
    path('etudiants/<int:pk>/edit/', EtudiantUpdate.as_view(), name='etudiant_edit'),
    path('etudiants/<int:pk>/delete/', EtudiantDelete.as_view(), name='etudiant_delete'),

    # UEs
    path('ues/', UEList.as_view(), name='ue_list'),
    path('ues/new/', UECreate.as_view(), name='ue_new'),
    path('ues/<str:pk>/edit/', UEUpdate.as_view(), name='ue_edit'),
    path('ues/<str:pk>/delete/', UEDelete.as_view(), name='ue_delete'),

    # Ressources
    path('ressources/', RessourceList.as_view(), name='ressource_list'),
    path('ressources/new/', RessourceCreate.as_view(), name='ressource_new'),
    path('ressources/<str:pk>/edit/', RessourceUpdate.as_view(), name='ressource_edit'),
    path('ressources/<str:pk>/delete/', RessourceDelete.as_view(), name='ressource_delete'),

    # Enseignants
    path('enseignants/', EnseignantList.as_view(), name='enseignant_list'),
    path('enseignants/new/', EnseignantCreate.as_view(), name='enseignant_new'),
    path('enseignants/<int:pk>/edit/', EnseignantUpdate.as_view(), name='enseignant_edit'),
    path('enseignants/<int:pk>/delete/', EnseignantDelete.as_view(), name='enseignant_delete'),

    # Examens
    path('examens/', ExamenList.as_view(), name='examen_list'),
    path('examens/new/', ExamenCreate.as_view(), name='examen_new'),
    path('examens/<int:pk>/edit/', ExamenUpdate.as_view(), name='examen_edit'),
    path('examens/<int:pk>/delete/', ExamenDelete.as_view(), name='examen_delete'),

    # Notes
    path('notes/', NoteList.as_view(), name='note_list'),
    path('notes/new/', NoteCreate.as_view(), name='note_new'),
    path('notes/<int:pk>/edit/', NoteUpdate.as_view(), name='note_edit'),
    path('notes/<int:pk>/delete/', NoteDelete.as_view(), name='note_delete'),

]
