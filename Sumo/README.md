# Sumo

## Downloads
Para realizar o download do SUMO, acesse o site oficial do projeto e siga as instruções para a instalação de acordo com o seu sistema operacional.

## Mapa

### OpenStreetMap: Local onde conseguir os mapas para a simulação

1. Acesse o site [OpenStreetMap](https://www.openstreetmap.org/).
2. Selecione a região do mapa que deseja usar para simulação.
3. Exporte o mapa no formato `.osm`.

## Conversão do mapa de `.osm` para `.xml`

1. Abra a pasta onde você instalou o SUMO e encontre a pasta `bin`.
2. Abra a pasta `bin` no terminal.
3. No terminal, execute o seguinte comando para converter o arquivo `.osm` para `.xml`:
   ```bash
   netconvert --osm-files file.osm -o file.net.xml
    ```
**Nota:** Se o arquivo `.osm` que deseja converter estiver em outro diretório, é necessário fornecer o caminho completo para o arquivo no lugar de `file.osm`.

## Executando o Sumo

1. Abra o SUMO.
2. Na aba **File**, clique em **Open Network**.
3. Navegue até o mapa convertido (`file.net.xml`) e selecione-o para carregar na simulação.
