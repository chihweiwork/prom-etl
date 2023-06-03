# prom-etl
利用prom-tool與pyspark將prometheus的資料下載出來整理成csv格式，根據metric與date儲存資料，適合把資料寫入HDFS中
## Install
使用 make 來安裝 prom-etl
``` bash
make all
```
## Run
### 使用 run.sh
```
bash run.sh [START/TIME] [END/TIME] [OUTPUT/FILE/PATH]
```
- 如果 promtool 的位置不一樣，必須修改 run.sh 中 promtool 的位置
- STAET TIME: 時間戳記
- END TIME: 時間戳記
- OUTPUT FILE PATH: 輸出的檔案的路徑
### 使用 Makefile
```
make run PROMTOOL=PATH/TO/PROMTOOL STIME=START/TIME ETIME=END/TIME PROMEDATA=PATH/TO/PROM/DATA  OUTPUT=PATH/TO/OUTPUT/FORDER
```
### 使用 python3 執行程式
``` bash
source PATH/TO/VENV/ACTIVATE
PROMTOOL/PATH/promtool tsdb dump --min-time=TIMESTAMP(ms) --max-time=TIMESTAMP(ms) PATH/TO/PROMETHEUS/DATA | python3 main.py --output PATH/TO/OUTPUT/FILE
```
## 解除安裝
``` bash
make clean
```
