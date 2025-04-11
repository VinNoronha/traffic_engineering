from qgis.PyQt.QtWidgets import QInputDialog, QProgressDialog, QApplication
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsWkbTypes,
    QgsFeatureRequest
)
import time

# Solicita ao usuário o nome da camada
layer_names = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
layer_name, ok = QInputDialog.getItem(None, "Selecionar camada", "Escolha a camada de entrada:", layer_names, editable=False)

if not ok or not layer_name:
    raise Exception("Nenhuma camada selecionada.")

layer = QgsProject.instance().mapLayersByName(layer_name)[0]

# Verifica se a geometria é do tipo linha
if layer.geometryType() != QgsWkbTypes.LineGeometry:
    raise Exception("A camada selecionada não possui geometria do tipo linha.")

# Prepara camada de saída
crs = layer.crs().authid()
uri = f"Point?crs={crs}&field=id:integer"
dangle_layer = QgsVectorLayer(uri, "Dangles", "memory")
dangle_provider = dangle_layer.dataProvider()

# Cria barra de progresso
total_features = layer.featureCount()
progress = QProgressDialog("Analisando dangles...", "Cancelar", 0, total_features)
progress.setWindowTitle("Processando Geometrias")
progress.setMinimumDuration(0)
progress.setValue(0)

count = 0

for feature in layer.getFeatures():
    if progress.wasCanceled():
        print("Processo cancelado pelo usuário.")
        break

    geom = feature.geometry()
    if geom.isEmpty():
        count += 1
        continue

    lines = []
    if geom.isMultipart():
        lines = geom.asMultiPolyline()
    else:
        line = geom.asPolyline()
        if line:
            lines = [line]

    for line in lines:
        endpoints = [line[0], line[-1]]
        disconnected_endpoints = []

        for endpoint in endpoints:
            point_geom = QgsGeometry.fromPointXY(QgsPointXY(endpoint))
            is_connected = False
            request = QgsFeatureRequest().setFilterRect(point_geom.boundingBox())

            for other_feature in layer.getFeatures(request):
                if other_feature.id() != feature.id() and other_feature.geometry().intersects(point_geom):
                    is_connected = True
                    break

            if not is_connected:
                disconnected_endpoints.append(point_geom)

        for point_geom in disconnected_endpoints:
            f = QgsFeature()
            f.setGeometry(point_geom)
            f.setAttributes([feature.id()])
            dangle_provider.addFeature(f)

    count += 1
    progress.setValue(count)
    QApplication.processEvents()  # Mantém a interface atualizada
    time.sleep(0.001)  # Pequeno delay para suavizar a carga (pode ajustar ou remover)

# Finaliza processo
progress.setValue(total_features)
QgsProject.instance().addMapLayer(dangle_layer)
print(f"Dangles identificados em {count} feições e adicionados à camada 'Dangles'.")
