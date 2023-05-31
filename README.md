# prom-etl
利用prom-tool與pyspark將prometheus2的資料下載出來整理成csv格式，根據metric與date儲存資料，適合把資料寫入HDFS中
## Install
使用 make 來安裝 prom-etl
``` bash
make all
```
## Run
```
bash run.sh [START/TIME] [END/TIME] [OUTPUT/FILE/PATH]
```
- STAET TIME: 時間戳記
- END TIME: 時間戳記
- OUTPUT FILE PATH: 輸出的檔案的路徑
## 解除安裝
``` bash
make clean
```
