# Author: Eduardo Alvarez
# mail: jesus.e.alvarez@gmail.com
# Date: 05/08/2024
# linkedin: www.linkedin.com/in/jesus-eduardo-alvarez-garcia

"""
Imagina que tienes un programa que necesita
 evaluar las calificaciones de los estudiantes y asignarles una letra según su puntuación. 
 Además, si un estudiante  tiene una puntuación menor a 60, se le asignará automáticamente una "F".

"""
calificaciones = (('D-', 60, 62),('D', 63, 66),('D+', 67, 69),('C-', 70, 72),('C', 73, 76),('C+', 77, 79),('B-', 80, 86),('B', 83, 86),('B+', 87, 89),('A', 90, 92),('A+', 93, 100))

def calificacionAlumno():

    calificacion = int(input('Cual fue la calificacion del estudiante? : '))

    for calif in calificaciones:
        if(calificacion < 60):
            print('F')
            calificacionAlumno()

        if(calificacion >= calif[1] and calificacion <= calif[2]):
            print(calif[0])
            calificacionAlumno()
            

calificacionAlumno()