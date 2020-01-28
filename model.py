import json

filename = 'prettydata.json'
with open(filename) as f:
    pop_data = json.load(f)
    allcases = []
    for value in pop_data:
        if (value['day'] == "1.26" and value['country'] == "中国"):
            area = value['area']
            confirm = value['confirm']
            case = []
            case.append(area)
            case.append(confirm)
            allcases.append(case)
            print(area + ": " + str(confirm) + " confirm cases.")

from snapshot_pyppeteer import snapshot
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import ChartType, SymbolType

def geo_heatmap() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "Confirmed Cases",
            allcases,
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Distribution of 2019-nCoV in China"),
        )
    )
    make_snapshot(snapshot, c.render(), "geo.png")

if __name__ == '__main__':
    geo_heatmap()