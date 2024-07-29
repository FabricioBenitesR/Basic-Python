def ingresar_datos():
    alumnos = [
        {
            'codigo': '1031300223',
            'nombre': 'Motta Fukumoto',
            'cursos': [
                {'curso': 'Análisis Matemático II', 'nota': 9, 'creditos': 4},
                {'curso': 'Física II', 'nota': 17, 'creditos': 4},
                {'curso': 'Microeconomía', 'nota': 14, 'creditos': 3},
                {'curso': 'Lenguaje de Programación', 'nota': 16, 'creditos': 4},
                {'curso': 'Diseño Gráfico', 'nota': 8, 'creditos': 3},
                {'curso': 'Química II', 'nota': 15, 'creditos': 4}
            ]
        },
        {
            'codigo': '1031300224',
            'nombre': 'A',
            'cursos': [
                {'curso': 'Análisis Matemático II', 'nota': 12, 'creditos': 4},
                {'curso': 'Física II', 'nota': 17, 'creditos': 4},
                {'curso': 'Microeconomía', 'nota': 14, 'creditos': 3},
                {'curso': 'Lenguaje de Programación', 'nota': 16, 'creditos': 4},
                {'curso': 'Diseño Gráfico', 'nota': 1, 'creditos': 3},
                {'curso': 'Química II', 'nota': 15, 'creditos': 4}
            ]
        },
        {
            'codigo': '1031300225',
            'nombre': 'B',
            'cursos': [
                {'curso': 'Análisis Matemático II', 'nota': 12, 'creditos': 4},
                {'curso': 'Física II', 'nota': 17, 'creditos': 4},
                {'curso': 'Microeconomía', 'nota': 14, 'creditos': 3},
                {'curso': 'Lenguaje de Programación', 'nota': 2, 'creditos': 4},
                {'curso': 'Diseño Gráfico', 'nota': 8, 'creditos': 3},
                {'curso': 'Química II', 'nota': 15, 'creditos': 4}
            ]
        },
        {
            'codigo': '1031300226',
            'nombre': 'C',
            'cursos': [
                {'curso': 'Análisis Matemático II', 'nota': 12, 'creditos': 4},
                {'curso': 'Física II', 'nota': 17, 'creditos': 4},
                {'curso': 'Microeconomía', 'nota': 14, 'creditos': 3},
                {'curso': 'Lenguaje de Programación', 'nota': 16, 'creditos': 4},
                {'curso': 'Diseño Gráfico', 'nota': 8, 'creditos': 3},
                {'curso': 'Química II', 'nota': 15, 'creditos': 4}
            ]
        },
        {
            'codigo': '1031300227',
            'nombre': 'D',
            'cursos': [
                {'curso': 'Análisis Matemático II', 'nota': 12, 'creditos': 4},
                {'curso': 'Física II', 'nota': 17, 'creditos': 4},
                {'curso': 'Microeconomía', 'nota': 14, 'creditos': 3},
                {'curso': 'Lenguaje de Programación', 'nota': 16, 'creditos': 4},
                {'curso': 'Diseño Gráfico', 'nota': 8, 'creditos': 3},
                {'curso': 'Química II', 'nota': 15, 'creditos': 4}
            ]
        }
    ]
    return alumnos

def listar_promedios(alumnos):
    print("\nListado de alumnos con su promedio ponderado:")
    for alumno in alumnos:
        total_puntos = sum(curso['nota'] * curso['creditos'] for curso in alumno['cursos'])
        total_creditos = sum(curso['creditos'] for curso in alumno['cursos'])
        promedio = total_puntos / total_creditos
        print(f"{alumno['nombre']}: {promedio:.2f}")

def detectar_mayor_promedio(alumnos):
    mayor_promedio = -1
    alumno_mayor_promedio = None
    for alumno in alumnos:
        total_puntos = sum(curso['nota'] * curso['creditos'] for curso in alumno['cursos'])
        total_creditos = sum(curso['creditos'] for curso in alumno['cursos'])
        promedio = total_puntos / total_creditos
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            alumno_mayor_promedio = alumno
    print(f"\nAlumno con el mayor promedio: {alumno_mayor_promedio['nombre']} con un promedio de {mayor_promedio:.2f}")

def reportar_desaprobados(alumnos):
    print("\nAlumnos desaprobados:")
    for alumno in alumnos:
        total_puntos = sum(curso['nota'] * curso['creditos'] for curso in alumno['cursos'])
        total_creditos = sum(curso['creditos'] for curso in alumno['cursos'])
        promedio = total_puntos / total_creditos
        if any(curso['nota'] < 14 for curso in alumno['cursos']) and promedio <= 13.5:
            print(alumno['nombre'])

def curso_con_mas_desaprobados(alumnos):
    desaprobados_por_curso = {}
    for alumno in alumnos:
        for curso in alumno['cursos']:
            if curso['nota'] < 14:
                if curso['curso'] in desaprobados_por_curso:
                    desaprobados_por_curso[curso['curso']] += 1
                else:
                    desaprobados_por_curso[curso['curso']] = 1
    curso_con_mas_desaprobados = max(desaprobados_por_curso, key=desaprobados_por_curso.get)
    print(f"\nCurso con más desaprobados: {curso_con_mas_desaprobados} con {desaprobados_por_curso[curso_con_mas_desaprobados]} desaprobados")

def main():
    alumnos = ingresar_datos()

    listar_promedios(alumnos)
    detectar_mayor_promedio(alumnos)
    reportar_desaprobados(alumnos)
    curso_con_mas_desaprobados(alumnos)

main()
