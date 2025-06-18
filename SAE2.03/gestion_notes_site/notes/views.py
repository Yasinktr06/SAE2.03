# notes/views.py

from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import (
    Etudiant,
    UE,
    Ressource,
    Enseignant,
    Examen,
    Note
)
from .forms import NoteForm


# --- CRUD Étudiant ---
class EtudiantList(ListView):
    model = Etudiant
    template_name = 'notes/etudiant_list.html'
    context_object_name = 'etudiants'

class EtudiantCreate(CreateView):
    model = Etudiant
    fields = '__all__'
    template_name = 'notes/etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')

class EtudiantUpdate(UpdateView):
    model = Etudiant
    fields = '__all__'
    template_name = 'notes/etudiant_form.html'
    success_url = reverse_lazy('etudiant_list')

class EtudiantDelete(DeleteView):
    model = Etudiant
    template_name = 'notes/etudiant_confirm_delete.html'
    success_url = reverse_lazy('etudiant_list')


# --- CRUD UE ---
class UEList(ListView):
    model = UE
    template_name = 'notes/ue_list.html'
    context_object_name = 'ues'

class UECreate(CreateView):
    model = UE
    fields = ['code', 'nom', 'semestre', 'credit_ects']
    template_name = 'notes/ue_form.html'
    success_url = reverse_lazy('ue_list')

class UEUpdate(UpdateView):
    model = UE
    fields = ['code', 'nom', 'semestre', 'credit_ects']
    template_name = 'notes/ue_form.html'
    success_url = reverse_lazy('ue_list')

class UEDelete(DeleteView):
    model = UE
    template_name = 'notes/ue_confirm_delete.html'
    success_url = reverse_lazy('ue_list')


# --- CRUD Ressource ---
class RessourceList(ListView):
    model = Ressource
    template_name = 'notes/ressource_list.html'
    context_object_name = 'ressources'

class RessourceCreate(CreateView):
    model = Ressource
    fields = ['code', 'nom', 'descriptif', 'coefficient', 'ue']
    template_name = 'notes/ressource_form.html'
    success_url = reverse_lazy('ressource_list')

class RessourceUpdate(UpdateView):
    model = Ressource
    fields = ['code', 'nom', 'descriptif', 'coefficient', 'ue']
    template_name = 'notes/ressource_form.html'
    success_url = reverse_lazy('ressource_list')

class RessourceDelete(DeleteView):
    model = Ressource
    template_name = 'notes/ressource_confirm_delete.html'
    success_url = reverse_lazy('ressource_list')


# --- CRUD Enseignant ---
class EnseignantList(ListView):
    model = Enseignant
    template_name = 'notes/enseignant_list.html'
    context_object_name = 'enseignants'

class EnseignantCreate(CreateView):
    model = Enseignant
    fields = ['prenom', 'nom']
    template_name = 'notes/enseignant_form.html'
    success_url = reverse_lazy('enseignant_list')

class EnseignantUpdate(UpdateView):
    model = Enseignant
    fields = ['prenom', 'nom']
    template_name = 'notes/enseignant_form.html'
    success_url = reverse_lazy('enseignant_list')

class EnseignantDelete(DeleteView):
    model = Enseignant
    template_name = 'notes/enseignant_confirm_delete.html'
    success_url = reverse_lazy('enseignant_list')


# --- CRUD Examen ---
class ExamenList(ListView):
    model = Examen
    template_name = 'notes/examen_list.html'
    context_object_name = 'examens'

class ExamenCreate(CreateView):
    model = Examen
    fields = ['titre', 'date', 'coefficient', 'ue', 'enseignant']
    template_name = 'notes/examen_form.html'
    success_url = reverse_lazy('examen_list')

class ExamenUpdate(UpdateView):
    model = Examen
    fields = ['titre', 'date', 'coefficient', 'ue', 'enseignant']
    template_name = 'notes/examen_form.html'
    success_url = reverse_lazy('examen_list')

class ExamenDelete(DeleteView):
    model = Examen
    template_name = 'notes/examen_confirm_delete.html'
    success_url = reverse_lazy('examen_list')


# --- CRUD Note ---
class NoteList(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

# notes/views.py (partie NoteCreate)
from django.db import IntegrityError

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['etudiant'].widget = forms.HiddenInput()
        etu_pk = self.request.GET.get('etudiant')
        if etu_pk:
            form.initial['etudiant'] = etu_pk
        return form

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        etu_pk = self.request.GET.get('etudiant')
        if etu_pk:
            ctx['etudiant_obj'] = get_object_or_404(Etudiant, pk=etu_pk)
        return ctx

    def form_valid(self, form):
        try:
            self.object = form.save()
        except IntegrityError:
            # si existant, on met à jour note & appreciation
            ex = form.cleaned_data['examen']
            et = form.cleaned_data['etudiant']
            existing = Note.objects.get(examen=ex, etudiant=et)
            existing.note = form.cleaned_data['note']
            existing.appreciation = form.cleaned_data.get('appreciation','')
            existing.save()
            self.object = existing
        return super().form_valid(form)

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['etudiant'].widget = forms.HiddenInput()
        return form

class NoteDelete(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
