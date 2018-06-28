from django.db import models

# Create your models here.

class Prevision(models.Model):
    Id_Prevision = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30)
    ESTADOS = (('A', 'Activo'), ('I', 'Inactivo'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='A')

    def __str__(self):
        return self.Descripcion

class Especialidad(models.Model):
    Id_Especialidad = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30)
    ESTADOS = (('A', 'Activo'), ('I', 'Inactivo'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='A')

    def __str__(self):
        return self.Descripcion


class Horario(models.Model):
    Id_Horario = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30)
    Entrada = models.DurationField()
    Salida = models.DurationField()

    def __str__(self):
        return self.Descripcion

class Genero(models.Model):
    Id_sexo = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30)
    ESTADOS = (('A', 'Activo'), ('I', 'Inactivo'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='A')

    def __str__(self):
        return self.Descripcion

class TipoIdentificacion(models.Model):
    Id_identificacion = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30)
    ESTADOS = (('A', 'Activo'), ('I', 'Inactivo'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='A')

    def __str__(self):
        return self.Descripcion


class Paciente(models.Model):
    Prevision = models.ForeignKey(Prevision, null=False, blank=False, on_delete=models.CASCADE)
    TipoIdentificacion = models.ForeignKey(TipoIdentificacion, null=False, blank=False, on_delete=models.CASCADE)
    Genero = models.ForeignKey(Genero, null=False, blank=False, on_delete=models.CASCADE)
    Rut = models.PositiveSmallIntegerField()
    Dv = models.CharField(max_length=1)
    Nombres = models.CharField(max_length=30)
    Apellido_Paterno = models.CharField(max_length=30)
    Apellido_Materno = models.CharField(max_length=30)
    Fecha_Nacimiento = models.DateField()
    Telefono = models.PositiveSmallIntegerField()
    Direccion = models.CharField(max_length=30)
    Comuna = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Apellido_Paterno, self.Apellido_Materno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Medico(models.Model):
    Especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)
    Horario = models.ForeignKey(Horario, null=False, blank=False, on_delete=models.CASCADE)
    Genero = models.ForeignKey(Genero, null=False, blank=False, on_delete=models.CASCADE)
    Id_Medico = models.AutoField(primary_key=True)
    Rut_Medico = models.PositiveSmallIntegerField()
    Dv_Medico = models.CharField(max_length=1)
    Nombres = models.CharField(max_length=100)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateField()

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Apellido_Paterno, self.Apellido_Materno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Consulta(models.Model):
    Id_Consulta = models.AutoField(primary_key=True)
    Medico = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_Consulta = models.DateField()
    ESTADOS = (('A', 'Activo'), ('I', 'Inactivo'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='A')

    def __str__(self):
        return "{0}, {1}, ({2})".format(self.Paciente, self.Medico, self.Fecha_Consulta)














