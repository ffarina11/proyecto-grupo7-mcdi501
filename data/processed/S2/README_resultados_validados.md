# Resultados validados — Sumativa 2 (Informe 3) | Grupo 7

MCDI501 Estadística Computacional para la Toma de Decisiones (UNAB).
Validación por remuestreo y simulación de los resultados de la Sumativa 1
(dataset Realinho et al., 2021; n binario = 3,630).

## Contenido
- `resultados_validados_S2.csv` — resultados de bootstrap, permutación, correlaciones,
  Monte Carlo y robustez, con veredicto y uso propuesto en S3 (sep = ';').
- `resultados_validados_S2.xlsx` — detalle por componente (6 hojas).

## Reproducción
1. Ubicar `data_predict_binario.csv` (S1) en `data/processed/` o junto al notebook.
2. Ejecutar `S2_Informe_3_grupo_7.ipynb` de inicio a fin (kernel Python 3.11+).
3. Semilla global 42; B = 10,000 remuestras; 50,000 iteraciones Monte Carlo.

Los resultados son asociaciones estadísticas dentro del dataset analizado y no acreditan causalidad.
