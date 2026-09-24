# Mini Exemplos de Recursos Nativos com Flet 🐍📱

Baseado na documentação oficial de *Services* do Flet:
https://flet.dev/docs/services/ (Battery, HapticFeedback, Geolocator,
Connectivity, SharedPreferences, Flashlight, LocalAuthentication e outros).

## ✅ Nota de revisão (Flet 1.0.0 — setembro/2026)

Cada um dos 9 arquivos foi conferido **linha a linha contra a documentação
oficial atual** de cada service (`flet.dev/docs/services/...`), comparando
nomes de classes, métodos, parâmetros e tipos de retorno. Isto é uma
revisão de código, não uma execução em dispositivo real — por isso os
comentários abaixo distinguem o que foi **verificado contra a doc** do que
seria bom você mesmo **testar num celular físico**.

## Como rodar

Cada arquivo é independente e roda sozinho:

```bash
python -m venv venv
Windows: venv\Scripts\activate
pip install "flet[all]" --upgrade
python 01_filepicker_selecionar.py
```

Para testar como app mobile de verdade (com câmera/GPS/sensores/biometria
reais), rode no seu celular com o app **Flet Studio**, ou publique com:

```bash
flet run --android main.py
flet run --ios main.py
```

Alguns exemplos exigem pacotes extras (indicados no topo do arquivo), por exemplo:

```bash
pip install --upgrade flet-geolocator flet-flashlight flet-local-auth
```

## Os 9 mini exemplos (recursos nativos)

| # | Arquivo | Recurso | O que mostra |
|---|---------|---------|---------------|
| 1 | `01_filepicker_selecionar.py` | FilePicker | Selecionar um ou vários arquivos e ver nome/tamanho |
| 2 | `02_battery.py` | Battery | Ler nível de bateria, estado e modo de economia |
| 3 | `03_haptic_feedback.py` | HapticFeedback | Disparar vibrações leve/média/forte e clique de seleção |
| 4 | `04_geolocator.py` | Geolocator | Pedir permissão e obter latitude/longitude do GPS + endereço |
| 5 | `05_connectivity.py` | Connectivity | Ver se está no wifi/dados móveis/offline, em tempo real |
| 6 | `06_shared_preferences.py` | SharedPreferences | Salvar e carregar um dado simples entre execuções |
| 7 | `07_flashlight.py` | Flashlight | Ligar e desligar a lanterna do celular |
| 8 | `08_notificacao.py` | Banner | Aviso persistente no topo da tela (não é notificação de sistema) |

## Observações importantes

- **Web vs Mobile**: alguns recursos (Flashlight, LocalAuthentication) não
  funcionam em navegador — só em Android/iOS/desktop (e LocalAuthentication
  também não funciona em Linux). O Geolocator e o FilePicker funcionam
  também na web, mas com pequenas diferenças (por exemplo,
  `save_file`/`get_directory_path` não funcionam em modo web).
- **Ações de cliques em navegador (iOS Safari)**: para `FilePicker.pick_files()`
  e `Share` funcionarem de forma confiável dentro de apps web no iPhone, a
  documentação recomenda usar as "client actions" (`ft.PickFiles`,
  `ft.ShareText`) ao invés de chamar o método direto num `on_click` — veja a
  seção "Picking files with a client action" na doc do FilePicker.
- **Permissões**: Geolocator, LocalAuthentication e Flashlight exigem
  permissões declaradas no build (`flet build apk/ipa --permissions ...`).
  Veja a seção "Requirements"/"Setup" de cada página de serviço.
- **Modelo de thread único (1.0)**: handlers síncronos agora rodam direto no
  loop de eventos, então operações bloqueantes (ex.: `requests.get`,
  `time.sleep`) travam a tela. Por isso o exemplo do Geolocator usa `httpx`
  (assíncrono) em vez de `requests`. Veja
  https://flet.dev/docs/updates/migrate-to-1-0/ para o guia completo.
- **Cuidado com `DurationValue`**: várias propriedades de duração no Flet
  (`time_limit`, `duration`, `period`, etc.) aceitam tanto `ft.Duration`
  quanto um `int` — mas esse `int` sempre representa **milissegundos**,
  nunca segundos. Foi exatamente esse detalhe que causou o bug corrigido
  no `04_geolocator.py`. Na dúvida, use sempre `ft.Duration(seconds=...)`
  explicitamente para deixar a intenção clara no código.
