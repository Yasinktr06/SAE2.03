# notes/forms.py

from django import forms
from django.utils import timezone
from .models import Note, Examen, Etudiant, UE, Enseignant
from .models import Ressource


class NoteForm(forms.ModelForm):
    etudiant = forms.ModelChoiceField(
        queryset=Etudiant.objects.all(),
        widget=forms.HiddenInput()
    )
    ue_number = forms.ChoiceField(
        choices=[(ue.code, ue.code) for ue in UE.objects.all()],
        label="UE associée"
    )
    examen_name = forms.CharField(
        max_length=200,
        label="Titre de l’examen"
    )
    enseignant = forms.ModelChoiceField(
        queryset=Enseignant.objects.all(),
        label="Enseignant"
    )
    ressource = forms.ModelChoiceField(
    queryset = Ressource.objects.all(),
    label = "Ressource",
    required = False  # Rendre ce champ optionnel si nécessaire

)

    class Meta:
        model = Note
        fields = [
            'etudiant',
            'ue_number',
            'examen_name',
            'enseignant',
            'ressource',  # Ajout de la ressource
            'note',
            'appreciation'
        ]

    def save(self, commit=True):
        # Extraction des champs personnalisés
        titre = self.cleaned_data.pop('examen_name')
        ue_num = self.cleaned_data.pop('ue_number')
        prof = self.cleaned_data.pop('enseignant')

        # Récupération de l'UE
        ue_obj = UE.objects.get(code=ue_num)
        today = timezone.now().date()

        # Création ou récupération de l'examen
        examen_obj, created = Examen.objects.get_or_create(
            titre=titre,
            defaults={
                'date': today,
                'coefficient': 1,  # Tu peux ajuster ce champ si besoin
                'ue': ue_obj,
                'enseignant': prof
            }
        )

        # Si l'examen existe déjà, on met à jour les champs nécessaires
        if not created:
            changed = False
            if examen_obj.ue != ue_obj:
                examen_obj.ue = ue_obj
                changed = True
            if examen_obj.enseignant != prof:
                examen_obj.enseignant = prof
                changed = True
            if examen_obj.date != today:
                examen_obj.date = today
                changed = True
            if changed:
                examen_obj.save()

        # Affectation de l'examen à la note et enregistrement
        self.instance.examen = examen_obj
        return super().save(commit)