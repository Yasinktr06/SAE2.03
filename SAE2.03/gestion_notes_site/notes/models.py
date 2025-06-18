from django.db import models

class Etudiant(models.Model):
    numero_etudiant = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    groupe = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class UE(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=200)
    semestre = models.CharField(max_length=20)
    credit_ects = models.IntegerField()

class Ressource(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=200)
    descriptif = models.TextField()
    coefficient = models.FloatField()
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)

# notes/models.py
class Enseignant(models.Model):
    nom    = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Examen(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateField()
    coefficient = models.FloatField()
    ue = models.ForeignKey(
        UE,
        on_delete=models.CASCADE,
        null=True,    # ← autorise NULL
        blank=True    # ← permet de ne pas le remplir
    )
    enseignant = models.ForeignKey(
        Enseignant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
class Note(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    note = models.FloatField()
    appreciation = models.TextField(blank=True, null=True)
    ressource = models.ForeignKey(Ressource, null=True, blank=True,
                                  on_delete=models.SET_NULL)  # Nouvelle ligne pour la ressource
    class Meta:
        unique_together = ('examen', 'etudiant')

