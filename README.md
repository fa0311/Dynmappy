# Dynmappy

Minecraft の Dynmap plugin を python で扱います<br>
Dynmap が必要です<br>

## Import

```python
import Dynmappy
```

## How to use

```python
dynmapPath = "plugins/dynmap/web/tiles/world/flat" #DynmapのPath flat以外も可
hstart = -4 #左側の座標
hend = 4 #右側の座標
vstart = -3 #下の座標
vend  = 3 #上の座標
dynmapSize = 1 #サイズ 0 ~ 5
dynmapOutputPath = "dynmap.jpn" #出力先ファイル opencvで利用できるものはいける
dynmapExistPath = "assets/image/128x128.png" #読み込み失敗時に表示する画像

Dynmappy(DynmapPath).output(hstart, hend, vstart, vend, dynmapSize, dynmapOutputPath, dynmapExistPath)
```

<br><br>

# DynmappyMove

これはとてもシンプルです<br>

## Import

```python
import DynmappyMove
```

## How to use

```python
config = [
    {
        "name": "world",  #ワールドの名前
        "x": 0, #読み込み時の座標 minecraftの座標ではない
        "y": 0  #読み込み時の座標 minecraftの座標ではない
    },
    {
        "name": "world_nether",
        "x": -4,
        "y": -3
    }
]
Instance = DynmappyMove(config)

Instance.up() #上に動く
Instance.down() #下に動く
Instance.right() #右に動く
Instance.left() #左に動く
```
